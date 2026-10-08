#!/usr/bin/env python3
"""Espace partagé MEDINA : consultation et garde des remises.

Avec fragment-unique-2026-10-08, les opérations historiques par cours sont
interdites. La garde vérifie les preuves enregistrées d'un fragment entier ;
elle ne réalise ni revue médicale ni certification CIM-11. Aucun fragment
incomplet ne peut être transmis, audité ou déclaré INJECTE par cet outil.
L'exception explicite de Vial du 8 octobre est contrôlée dans un registre
provisoire distinct ; elle ne remplace ni l'audit final ni les verrous INJECTE.

  python3 tools/espace.py deposer  <dossier_lot> --auteur Claude|Codex
  python3 tools/espace.py ouvrir   <CODE>          # lecture seule sous le nouveau protocole
  python3 tools/espace.py consulter <ID_FRAGMENT>
  python3 tools/espace.py auditer  <CODE> --auditeur Claude|Codex --verdict favorable|favorable_sous_reserves_mineures|defavorable --rapport "<texte ou lien>"
  python3 tools/espace.py injecter <CODE>
  python3 tools/espace.py garde <avant> <apres>    # CI
"""
import argparse, hashlib, json, os, pathlib, re, shutil, subprocess, sys
try:
    from provisional_integration import ProvisionalError, validate_provisional
except ModuleNotFoundError as error:
    if error.name != "provisional_integration":
        raise
    from tools.provisional_integration import ProvisionalError, validate_provisional
R = pathlib.Path(__file__).resolve().parents[1]
W = R.parent / "medina_espace"
ESP = {"Claude": "espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX", "Codex": "espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE"}
OK = {"favorable", "favorable_sous_reserves_mineures"}
CANON = ("chapters/", "glossary/", "chapters.json")
FRAGMENT_STATUS = "organisation/fragment_status.json"
FRAGMENT_REGISTRY = "organisation/fragments.json"
PROTOCOL = "fragment-unique-2026-10-08"
STATES = {"A_COMPLETER", "EN_PRODUCTION", "PRET_A_TRANSMETTRE",
          "EN_AUDIT_CROISE", "AUDITE", "INJECTE"}
INITIAL_STATES = {"A_COMPLETER", "EN_PRODUCTION"}
ACTORS = {"Claude", "Codex"}


class FragmentError(ValueError):
    pass


def canonical(path):
    return path == "chapters.json" or path.startswith(("chapters/", "glossary/"))


def safe_path(value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise FragmentError(f"Chemin relatif sûr requis : {value!r}")
    path = pathlib.PurePosixPath(value)
    if (path.is_absolute() or str(path) != value or
            any(part in {".", ".."} for part in path.parts) or
            re.match(r"^[A-Za-z]:", value) or any(c in value for c in "\n\r\x00")):
        raise FragmentError(f"Chemin relatif sûr requis : {value!r}")
    return value


def hashes(value, description):
    if not isinstance(value, dict) or not value:
        raise FragmentError(f"{description} : inventaire de fichiers vide ou absent.")
    for path, digest in value.items():
        safe_path(path)
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise FragmentError(f"{description} : SHA-256 invalide pour {path}.")
    return value


def json_data(data, description):
    try:
        return json.loads(data.decode("utf-8"))
    except (ValueError, UnicodeError, AttributeError) as error:
        raise FragmentError(f"{description} : JSON UTF-8 illisible.") from error


class GitTree:
    """Lecture des blobs d'un commit local, sans checkout, fetch ni écriture."""

    def __init__(self, root, revision):
        self.root, self.revision, self.cache = root, revision, {}
        result = subprocess.run(["git", "ls-tree", "-rz", "--full-tree", revision],
                                cwd=root, capture_output=True)
        if result.returncode:
            raise FragmentError(f"Révision Git illisible : {revision}.")
        self.entries = {}
        for record in result.stdout.split(b"\0"):
            if record:
                metadata, path = record.split(b"\t", 1)
                mode, kind, oid = metadata.decode("ascii").split()
                self.entries[path.decode("utf-8")] = (mode, kind, oid)

    def read(self, path, required=True):
        safe_path(path)
        entry = self.entries.get(path)
        if entry is None:
            if required:
                raise FragmentError(f"Fichier absent à {self.revision} : {path}.")
            return None
        mode, kind, oid = entry
        if kind != "blob" or mode not in {"100644", "100755"}:
            raise FragmentError(f"Source ou preuve non régulière interdite : {path}.")
        if path not in self.cache:
            result = subprocess.run(["git", "cat-file", "blob", oid],
                                    cwd=self.root, capture_output=True)
            if result.returncode:
                raise FragmentError(f"Blob illisible : {path}.")
            self.cache[path] = result.stdout
        return self.cache[path]


def fragment_records(tree):
    raw = tree.read(FRAGMENT_STATUS, required=False)
    if raw is None:
        return None
    data = json_data(raw, FRAGMENT_STATUS)
    if (not isinstance(data, dict) or data.get("schema_version") != 1 or
            data.get("protocol") != PROTOCOL):
        raise FragmentError("Registre des fragments : protocole ou schéma invalide.")
    records = data.get("fragments")
    registry = json_data(tree.read(FRAGMENT_REGISTRY), FRAGMENT_REGISTRY)
    if not isinstance(records, list) or len(records) != 22 or not isinstance(registry, list) or len(registry) != 22:
        raise FragmentError("Le périmètre fixe doit contenir exactement 22 fragments.")
    expected = {f.get("id"): f.get("label") for f in registry if isinstance(f, dict)}
    by_id = {f.get("id"): f for f in records if isinstance(f, dict)}
    if len(expected) != 22 or len(by_id) != 22 or set(by_id) != set(expected):
        raise FragmentError("Identifiants de fragments manquants, ajoutés ou dupliqués.")
    for ident, fragment in by_id.items():
        if fragment.get("label") != expected[ident] or fragment.get("status") not in STATES:
            raise FragmentError(f"{ident} : libellé ou statut invalide.")
        if type(fragment.get("complete")) is not bool:
            raise FragmentError(f"{ident} : complete doit être un booléen explicite.")
        if not isinstance(fragment.get("coverage"), dict) or not isinstance(fragment.get("locked_files"), dict):
            raise FragmentError(f"{ident} : couverture ou verrou absent.")
        for field in ("internal_review", "cross_audit", "injection"):
            if field not in fragment or (fragment[field] is not None and not isinstance(fragment[field], dict)):
                raise FragmentError(f"{ident} : preuve {field} invalide.")
        real_proofs = fragment["complete"] or any(fragment[f] is not None for f in ("internal_review", "cross_audit", "injection"))
        if real_proofs and fragment.get("owner") not in ACTORS:
            raise FragmentError(f"{ident} : auteur Claude ou Codex requis pour une remise réelle.")
        if not isinstance(fragment.get("owner"), str) or not fragment["owner"].strip():
            raise FragmentError(f"{ident} : auteur absent.")
    return by_id


def document_proof(tree, path, digest, description):
    path = safe_path(path)
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise FragmentError(f"{description} : empreinte de rapport absente ou invalide.")
    data = tree.read(path)
    if not data.strip() or hashlib.sha256(data).hexdigest() != digest:
        raise FragmentError(f"{description} : rapport vide ou empreinte différente : {path}.")
    return data


def source_proof(tree, proof, description):
    files = hashes(proof.get("files"), description)
    source_dir = safe_path(proof.get("source_dir"))
    for path, digest in files.items():
        data = tree.read(f"{source_dir}/{path}")
        if hashlib.sha256(data).hexdigest() != digest:
            raise FragmentError(f"{description} : empreinte source différente : {path}.")
    actual = {p[len(source_dir) + 1:] for p in tree.entries if p.startswith(source_dir + "/")}
    if actual != set(files):
        raise FragmentError(f"{description} : sources absentes de l'inventaire ou fichiers manquants.")
    if not any(canonical(path) for path in files):
        raise FragmentError(f"{description} : aucune source médicale dans la remise.")
    return files


def ready_fragment(tree, fragment):
    ident = fragment["id"]
    coverage, review = fragment["coverage"], fragment["internal_review"]
    if (fragment["complete"] is not True or coverage.get("status") != "verifiee" or
            coverage.get("scope") != "fragment_complet" or not review):
        raise FragmentError(f"{ident} : fragment incomplet, couverture ou auto-revue non établie.")
    files = hashes(coverage.get("files"), f"{ident} couverture")
    inventory = json_data(document_proof(tree, coverage.get("inventory_path"),
                                        coverage.get("inventory_sha256"), f"{ident} inventaire"), "Inventaire de couverture")
    if (not isinstance(inventory, dict) or inventory.get("fragment_id") != ident or
            inventory.get("scope") != "fragment_complet" or inventory.get("complete") is not True or
            inventory.get("files") != files or inventory.get("uncovered_categories") != [] or
            not isinstance(inventory.get("categories"), list) or not inventory["categories"]):
        raise FragmentError(f"{ident} : inventaire complet structuré non établi.")
    if review.get("reviewer") != fragment["owner"] or review.get("scope") != "fragment_complet":
        raise FragmentError(f"{ident} : auto-revue intégrale de l'auteur requise.")
    document_proof(tree, review.get("report_path"), review.get("report_sha256"), f"{ident} auto-revue")
    if source_proof(tree, review, f"{ident} auto-revue") != files:
        raise FragmentError(f"{ident} : auto-revue sur une autre remise que l'inventaire.")
    return files


def swiss_context_proof(tree, audit, ident, final):
    """Require a reviewed, source-bound Swiss decision matrix before final audit.

    This checks the evidence contract, not the medical truth of quotations or
    applicability. The other AI must verify those against the originals.
    """
    proof = audit.get("swiss_context")
    if not isinstance(proof, dict) or proof.get("verdict") != "conforme":
        raise FragmentError(f"{ident} : contexte suisse non conforme ou absent ; audit défavorable requis.")
    raw = document_proof(tree, proof.get("matrix_path"), proof.get("matrix_sha256"),
                         f"{ident} matrice du contexte suisse")
    matrix = json_data(raw, f"{ident} matrice du contexte suisse")
    if (not isinstance(matrix, dict) or matrix.get("schema_version") != 1 or
            matrix.get("fragment_id") != ident or matrix.get("scope") != "fragment_complet" or
            matrix.get("source_files") != final or matrix.get("unresolved_divergences") != []):
        raise FragmentError(f"{ident} : matrice suisse incomplète, non liée aux sources finales ou divergence ouverte.")
    decisions = matrix.get("decisions")
    if not isinstance(decisions, list) or not decisions:
        raise FragmentError(f"{ident} : aucune décision clinique dans la matrice suisse.")
    chapters = {m.group(1) for path in final
                if (m := re.fullmatch(r"chapters/([A-Z][0-9]{2})/\1_[abcd]\.html", path))}
    drug_chapters = {m.group(1) for path in final
                     if (m := re.fullmatch(r"chapters/([A-Z][0-9]{2})/\1_d\.html", path))}
    documented, documented_drugs, identifiers = set(), set(), set()
    for row in decisions:
        if not isinstance(row, dict):
            raise FragmentError(f"{ident} : ligne invalide de la matrice suisse.")
        code, key, kind = row.get("chapter_code"), row.get("id"), row.get("kind")
        if (not isinstance(code, str) or code not in chapters or
                not isinstance(key, str) or not key.strip() or
                key in identifiers or kind not in {"diagnostic", "treatment", "medication", "follow_up"} or
                not isinstance(row.get("claim"), str) or not row["claim"].strip() or
                row.get("auditor_verdict") != "conforme" or
                row.get("divergence_status") not in {"none", "resolved"} or
                row.get("initial_primary_origin") not in {"swiss", "european", "american"} or
                row.get("final_primary_origin") not in {"swiss", "european", "american"}):
            raise FragmentError(f"{ident} : décision suisse non documentée ou non conforme : {key!r}.")
        identifiers.add(key)
        documented.add(code)
        swiss = row.get("swiss_guideline")
        required = ("organization", "title", "url", "version_date", "section", "passage")
        if not isinstance(swiss, dict) or swiss.get("status") not in {"applicable", "documented_gap"}:
            raise FragmentError(f"{ident} : source de société savante suisse absente : {key!r}.")
        if swiss["status"] == "applicable":
            if (any(not isinstance(swiss.get(field), str) or not swiss[field].strip()
                    for field in required) or not swiss["url"].startswith("https://")):
                raise FragmentError(f"{ident} : passage suisse applicable imprécis : {key!r}.")
        elif (any(not isinstance(swiss.get(field), str) or not swiss[field].strip()
                  for field in ("searched_on", "search_scope", "searched_sources", "gap_reason")) or
              row["final_primary_origin"] == "swiss"):
            raise FragmentError(f"{ident} : absence de directive suisse non démontrée : {key!r}.")
        foreign = row.get("foreign_sources", [])
        if not isinstance(foreign, list):
            raise FragmentError(f"{ident} : sources étrangères non documentées : {key!r}.")
        foreign_origins = set()
        for source in foreign:
            if (not isinstance(source, dict) or source.get("origin") not in {"european", "american"} or
                    any(not isinstance(source.get(field), str) or not source[field].strip()
                        for field in required) or not source["url"].startswith("https://")):
                raise FragmentError(f"{ident} : source étrangère imprécise : {key!r}.")
            foreign_origins.add(source["origin"])
        expected_foreign = {origin for origin in (row["initial_primary_origin"], row["final_primary_origin"])
                            if origin != "swiss"}
        if not expected_foreign.issubset(foreign_origins):
            raise FragmentError(f"{ident} : origine étrangère sans passage vérifiable : {key!r}.")
        if kind == "medication":
            documented_drugs.add(code)
            fi = row.get("swissmedic_product")
            fields = ("product_name", "authorization_number", "url", "accessed_on", "section", "passage")
            if (not isinstance(fi, dict) or any(not isinstance(fi.get(field), str) or
                    not fi[field].strip() for field in fields) or not fi["url"].startswith("https://")):
                raise FragmentError(f"{ident} : FI Swissmedic du produit exact absente : {key!r}.")
        if row["divergence_status"] == "resolved" and not str(row.get("resolution", "")).strip():
            raise FragmentError(f"{ident} : divergence sans arbitrage clinique : {key!r}.")
        if row["final_primary_origin"] != "swiss" and not str(row.get("resolution", "")).strip():
            raise FragmentError(f"{ident} : source non suisse retenue sans justification locale : {key!r}.")
        if row["final_primary_origin"] == "american" and not str(row.get("swiss_european_gap", "")).strip():
            raise FragmentError(f"{ident} : prescription américaine sans justification du manque suisse/européen : {key!r}.")
    if chapters != documented or drug_chapters != documented_drugs:
        raise FragmentError(f"{ident} : chaque cours et onglet pharmacologique doit figurer dans la matrice suisse.")


def audit_fragment(tree, fragment, original):
    audit, ident = fragment["cross_audit"], fragment["id"]
    other = next(iter(ACTORS - {fragment["owner"]}))
    if (audit.get("auditor") != other or audit.get("scope") != "fragment_complet" or
            audit.get("verdict") not in OK or audit.get("input_files") != original):
        raise FragmentError(f"{ident} : audit croisé unique de l'autre IA sur la remise complète requis.")
    document_proof(tree, audit.get("report_path"), audit.get("report_sha256"), f"{ident} audit croisé")
    final = source_proof(tree, audit, f"{ident} audit croisé")
    if not set(original).issubset(final):
        raise FragmentError(f"{ident} : audit supprimant une partie de la remise complète.")
    swiss_context_proof(tree, audit, ident, final)
    return final


def validate_fragment_guard(before, after):
    old, new = fragment_records(before), fragment_records(after)
    if old is not None and new is None:
        raise FragmentError("Suppression du registre ou abandon du protocole interdit.")
    if new is None:
        return None
    changed = {p for p in before.entries.keys() | after.entries.keys()
               if before.entries.get(p) != after.entries.get(p)}
    changed_medical = {p for p in changed if canonical(p)}
    if old is None:
        if changed_medical:
            raise FragmentError("Activation du protocole : modification médicale sans remise initiale préexistante.")
        for ident, fragment in new.items():
            if (fragment["status"] not in INITIAL_STATES or fragment["complete"] or
                    any(fragment[f] is not None for f in ("internal_review", "cross_audit", "injection")) or
                    fragment["locked_files"]):
                raise FragmentError(f"{ident} : activation avec fragment prétendument validé ou injecté interdite.")
        return []
    if set(old) != set(new):
        raise FragmentError("Ajout ou suppression de fragment interdit.")
    authorized = {}
    locked = {}
    errors = []
    for ident, fragment in new.items():
        previous = old[ident]
        if any(fragment[key] != previous[key] for key in ("id", "label")):
            raise FragmentError(f"{ident} : identité du fragment modifiée.")
        if fragment["owner"] != previous["owner"]:
            unresolved = (previous["owner"] not in ACTORS and previous["status"] in INITIAL_STATES and
                          not previous["complete"] and not previous["locked_files"] and
                          all(previous[key] is None for key in ("internal_review", "cross_audit", "injection")))
            if not unresolved or fragment["owner"] not in ACTORS:
                raise FragmentError(f"{ident} : auteur d'un fragment déjà attribué ou remis modifié.")
        if previous["status"] == "INJECTE":
            if fragment != previous:
                raise FragmentError(f"{ident} : INJECTE immuable ; réouverture ou modification du registre interdite.")
        if previous["cross_audit"] is not None and fragment["cross_audit"] != previous["cross_audit"]:
            raise FragmentError(f"{ident} : second audit ou retrait de l'audit unique interdit.")
        if previous["cross_audit"] is not None and any(fragment[key] != previous[key] for key in ("coverage", "internal_review", "complete")):
            raise FragmentError(f"{ident} : remise validée modifiée après audit unique.")
        ready = (fragment["complete"] or fragment["internal_review"] is not None or
                 fragment["cross_audit"] is not None or fragment["injection"] is not None or
                 fragment["status"] not in INITIAL_STATES)
        initial = ready_fragment(after, fragment) if ready else None
        final = audit_fragment(after, fragment, initial) if fragment["cross_audit"] is not None else None
        if fragment["cross_audit"] is not None and previous["cross_audit"] is None:
            original = ready_fragment(before, previous)
            if any(fragment[key] != previous[key] for key in ("coverage", "internal_review", "complete")) or original != initial:
                raise FragmentError(f"{ident} : audit sans remise complète et auto-revue préexistantes.")
        if fragment["status"] in {"AUDITE", "INJECTE"} and final is None:
            raise FragmentError(f"{ident} : statut sans audit croisé favorable.")
        if fragment["status"] != "INJECTE":
            if fragment["locked_files"] or fragment["injection"] is not None:
                raise FragmentError(f"{ident} : injection ou verrou sans statut INJECTE.")
            continue
        injection = fragment["injection"]
        if (not injection or injection.get("injector") != fragment["cross_audit"]["auditor"] or
                injection.get("files") != final or fragment["locked_files"] != final):
            raise FragmentError(f"{ident} : injection par l'auditeur et verrou des empreintes finales requis.")
        for path, digest in final.items():
            if path in locked and locked[path] != digest:
                raise FragmentError(f"{ident} : verrou incompatible sur source partagée : {path}.")
            locked[path] = digest
            data = after.read(path)
            if hashlib.sha256(data).hexdigest() != digest:
                raise FragmentError(f"{ident} : contenu injecté différent de l'audit ou supprimé : {path}.")
            if previous["status"] == "INJECTE":
                if before.read(path) != data or before.entries.get(path) != after.entries.get(path):
                    raise FragmentError(f"{ident} : source médicale verrouillée modifiée : {path}.")
            else:
                authorized[path] = digest
    # Vial's explicit 8 October exception is documented independently from
    # final fragment review/injection. It cannot reopen an INJECTE fragment.
    try:
        provisional = validate_provisional(before, after, old, new)
    except ProvisionalError as error:
        raise FragmentError(str(error)) from error
    for path, digest in provisional.items():
        if path in locked:
            raise FragmentError(f"Provisoire : source d'un fragment INJECTE verrouillée : {path}.")
        authorized[path] = digest
    for path in changed_medical:
        data = after.read(path, required=False)
        if data is None or authorized.get(path) != hashlib.sha256(data).hexdigest():
            errors.append(path)
    return errors


def protocol_active(root):
    path = pathlib.Path(root) / FRAGMENT_STATUS
    if not path.exists():
        return False
    data = json_data(path.read_bytes(), FRAGMENT_STATUS)
    if not isinstance(data, dict) or data.get("protocol") != PROTOCOL:
        raise FragmentError("Registre des fragments invalide ; opération refusée.")
    return True


def refuse_chapter_operation(action, root=None):
    if protocol_active(root or R):
        raise FragmentError(f"REFUS : {action} par cours/remise partielle interdit. "
                            "Le fragment entier doit être complet et auto-revu avant transmission ; "
                            "audit croisé unique puis injection par l'autre IA. "
                            "Cet outil fournit consultation et garde des preuves, sans produire ces revues.")


def consulter(cible):
    """Consulter le checkout actuel sans fetch, checkout, dépôt ou publication."""
    status = R / FRAGMENT_STATUS
    if status.exists():
        data = json_data(status.read_bytes(), FRAGMENT_STATUS)
        fragment = next((f for f in data.get("fragments", []) if cible in (f.get("id"), f.get("label"))), None)
        if fragment is not None:
            print(json.dumps(fragment, ensure_ascii=False, indent=2))
            return
    if not re.fullmatch(r"[A-Z][0-9]{2}", cible):
        raise FragmentError(f"Fragment ou cours inconnu : {cible}.")
    for base in ESP.values():
        path = R / base / cible
        if path.is_dir():
            print(path)
            return
    path = R / "chapters" / cible
    if not path.is_dir():
        raise FragmentError(f"Cours absent du checkout : {cible}.")
    print(path)

def git(*a, cwd=W, ok=True):
    r = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True)
    if ok and r.returncode: sys.exit(f"git {' '.join(a)} : {r.stderr.strip()}")
    return r.stdout

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def main_frais():
    git("fetch", "-q", "origin", "main", cwd=R)
    if not W.exists(): git("worktree", "add", "-q", "--detach", str(W), "origin/main", cwd=R)
    else: git("checkout", "-q", "--detach", "origin/main")

def pousser(msg, *chemins):
    git("add", *chemins); git("commit", "-q", "-m", msg)
    for _ in range(3):
        if subprocess.run(["git", "push", "-q", "origin", "HEAD:main"], cwd=W).returncode == 0: return
        git("pull", "-q", "--rebase", "origin", "main")
    sys.exit("Poussée impossible après trois essais.")

def dossier(code):
    for auteur, base in ESP.items():
        d = W / base / code
        if (d / "ETAT.json").exists(): return d, auteur
    sys.exit(f"{code} absent de l'espace partagé.")

def empreintes(d): return {str(p.relative_to(d / "sources")): sha(p) for p in sorted((d / "sources").rglob("*")) if p.is_file()}

def deposer(lot, auteur):
    refuse_chapter_operation("deposer")
    lot = pathlib.Path(lot).resolve(); m = json.loads((lot / "livraison.json").read_text())
    code = m["chapters"][0]["code"]; main_frais()
    refuse_chapter_operation("deposer", W)
    d = W / ESP[auteur] / code
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(lot / "sources", d / "sources")
    if (lot / "rapport.md").exists(): shutil.copy2(lot / "rapport.md", d / "rapport_auteur.md")
    base = {f["target_path"]: f.get("sha256") for f in m["files"]}
    etat = {"code": code, "titre": m["chapters"][0].get("title"), "auteur": auteur, "statut": "a_auditer",
            "base_main": base, "fichiers": empreintes(d), "audits": []}
    (d / "ETAT.json").write_text(json.dumps(etat, ensure_ascii=False, indent=1) + "\n")
    pousser(f"Espace partagé : {auteur} dépose {code} pour audit", str(d.relative_to(W)))
    print(f"Déposé : {d.relative_to(W)}")

def auditer(code, auditeur, verdict, rapport):
    refuse_chapter_operation("auditer")
    main_frais(); refuse_chapter_operation("auditer", W); d, auteur = dossier(code)
    if auditeur == auteur: sys.exit("REFUS : l'auteur ne peut pas auditer son propre cours.")
    e = json.loads((d / "ETAT.json").read_text()); e["fichiers"] = empreintes(d)
    e["audits"].append({"auditeur": auditeur, "verdict": verdict, "rapport": rapport, "fichiers": e["fichiers"]})
    e["statut"] = "audite_favorable" if verdict in OK else "a_corriger"
    (d / "ETAT.json").write_text(json.dumps(e, ensure_ascii=False, indent=1) + "\n")
    pousser(f"Espace partagé : {auditeur} audite {code} ({verdict})", str(d.relative_to(W)))

def injecter(code):
    refuse_chapter_operation("injecter")
    main_frais(); refuse_chapter_operation("injecter", W); d, auteur = dossier(code); e = json.loads((d / "ETAT.json").read_text()); f = empreintes(d)
    a = next((x for x in reversed(e["audits"]) if x["auditeur"] != auteur and x["verdict"] in OK and x["fichiers"] == f), None)
    if not a: sys.exit("REFUS : aucun audit croisé favorable sur les empreintes actuelles.")
    for cible in f:
        actuel = sha(W / cible) if (W / cible).exists() else None
        if actuel != e["base_main"].get(cible): sys.exit(f"REFUS : {cible} a changé sur main ; redéposer le lot rebasé.")
        (W / cible).parent.mkdir(parents=True, exist_ok=True); shutil.copy2(d / "sources" / cible, W / cible)
    env = {**os.environ, "MEDINA_OUT": str(W / ".qa"), "MEDINA_FRAGMENTS": str(W / ".qa/fragments")}
    codes = sorted({c.split("/")[1] for c in f if c.startswith("chapters/")})
    for cmd in (["python3", "test_v7.py", "--static", *codes], ["python3", "build_front.py", "--all-fragments"],
                ["python3", "tests/audit_fragments.py"], ["python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]):
        r = subprocess.run(cmd, cwd=W, capture_output=True, text=True, env=env)
        if r.returncode: git("checkout", "-q", "--", "."); sys.exit(f"REFUS : échec {' '.join(cmd)}\n{r.stdout[-1000:]}{r.stderr[-1000:]}")
    e["statut"] = "injecte"; (d / "ETAT.json").write_text(json.dumps(e, ensure_ascii=False, indent=1) + "\n")
    pousser(f"Injecter {code} ({auteur}) après audit croisé de {a['auditeur']}", *f, str(d.relative_to(W)))
    print(f"Injecté : {code}")

def garde(av, ap):
    try:
        before, after = GitTree(R, av), GitTree(R, ap)
        errors = validate_fragment_guard(before, after)
        if errors is not None:
            print("Sources médicales modifiées sans preuve admissible (audit final ou exception provisoire Vial) :", errors or "aucune")
            return 1 if errors else 0
    except FragmentError as error:
        print(f"REFUS garde-espace : {error}")
        return 1
    # Compatibilité des historiques sans registre ; ces audits par cours sont
    # inapplicables dès activation du protocole de remise par fragment entier.
    etats = []
    for base in ESP.values():
        for p in subprocess.run(["git", "ls-tree", "-r", "--name-only", ap, base], cwd=R, capture_output=True, text=True).stdout.split():
            if p.endswith("/ETAT.json"):
                e = json.loads(subprocess.run(["git", "show", f"{ap}:{p}"], cwd=R, capture_output=True, text=True).stdout)
                etats += [x["fichiers"] for x in e["audits"] if x["auditeur"] != e["auteur"] and x["verdict"] in OK]
    err = []
    for p in subprocess.run(["git", "diff", "--name-only", f"{av}..{ap}"], cwd=R, capture_output=True, text=True).stdout.split():
        if not canonical(p): continue
        b = subprocess.run(["git", "show", f"{ap}:{p}"], cwd=R, capture_output=True).stdout
        if not b or not any(x.get(p) == hashlib.sha256(b).hexdigest() for x in etats): err.append(p)
    print("Sources canoniques modifiées sans audit croisé :", err or "aucune"); return 1 if err else 0

def ouvrir(code):
    if protocol_active(R):
        return consulter(code)
    main_frais()
    if protocol_active(W):
        raise FragmentError("Le nouveau protocole interdit la copie de correction par cours ; consulter le checkout actuel.")
    print(W / dossier(code)[0].relative_to(W))


def main():
    a = sys.argv[1:]
    if a[:1] == ["garde"]:
        if len(a) != 3:
            raise FragmentError("Usage : espace.py garde <avant> <apres>")
        return garde(a[1], a[2])
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("deposer", "ouvrir", "consulter", "auditer", "injecter")); p.add_argument("cible")
    p.add_argument("--auteur", choices=sorted(ACTORS)); p.add_argument("--auditeur", choices=sorted(ACTORS)); p.add_argument("--verdict", choices=sorted(OK | {"defavorable"})); p.add_argument("--rapport", default="")
    x = p.parse_args(a)
    {"deposer": lambda: deposer(x.cible, x.auteur), "ouvrir": lambda: ouvrir(x.cible), "consulter": lambda: consulter(x.cible),
     "auditer": lambda: auditer(x.cible, x.auditeur, x.verdict, x.rapport), "injecter": lambda: injecter(x.cible)}[x.action]()
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (FragmentError, OSError, KeyError, ValueError) as error:
        sys.exit(str(error))
