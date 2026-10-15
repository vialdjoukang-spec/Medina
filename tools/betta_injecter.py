#!/usr/bin/env python3
"""Injection canonique des leçons Betta à l'état LIVRE (instruction de Vial, 15 octobre 2026).

Pour chaque leçon LIVRE (ou les codes donnés) : copie chapters/<CODE>/ et glossary/<code>.py
vers la racine, état INJECTE + empreintes « canonical » dans organisation/betta_status.json,
ligne chapters.json (audit différé non effectué), empreinte de chapters.json dans
nosology/integrity.json. La garde tools/betta_cycle.py vérifie ensuite chaque empreinte.
Ne touche aucun fichier de la chaîne des cycles 1–30 (CYCLES_CLAUDE.json, travail/, cycle_claude).
Usage : python3 tools/betta_injecter.py [--novo] [CODE ...]   (--novo : Projet Novo_12)

Novo_12 : sélection complète du lot déclaré, contrôlée en mémoire avant copie ;
dépôt et injection peuvent partager une PR. L'audit reste différé, non réalisé.
Retour arrière sur erreur ordinaire, sans effacer un travail concurrent ; une
interruption brutale du processus/système ne constitue pas une transaction atomique.
"""
import copy, fcntl, hashlib, json, os, shutil, sys, tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WAVE = {"S08": 6, "S05": 4, "S04": 3, "S06": 8}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def charger(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def ecrire(rel, data, compact=False, nl=True):
    texte = json.dumps(data, ensure_ascii=False, separators=(",", ":")) if compact else json.dumps(data, ensure_ascii=False, indent=2)
    (ROOT / rel).write_text(texte + ("\n" if nl else ""), encoding="utf-8")


class _Tree:
    """Snapshot used to validate a proposed Novo transaction before copying."""
    def __init__(self, files):
        self.files = files
        self.root = ROOT
        self.entries = {p: ("100644", "blob", hashlib.sha256(raw).hexdigest()) for p, raw in files.items()}

    def read(self, path, required=True):
        if required and path not in self.files:
            raise ValueError("Source ou preuve absente : " + str(path))
        return self.files.get(path)


def _novo_prepare(cibles, plan, status, rows):
    """Delivery + injection may share a PR; all declared lessons must be ready.

    Audits remain deferred and are never marked performed by this transaction.
    Validate source bytes, research gate, complete selection and catalogue first.
    """
    try:
        from tools import betta_cycle as G
    except ModuleNotFoundError:
        import betta_cycle as G
    try:
        from tools import publication_en_etat as P
    except ModuleNotFoundError:
        import publication_en_etat as P
    files = {}

    def read(path):
        G._req(isinstance(path, str) and not Path(path).is_absolute() and '..' not in path.split('/') and '\\' not in path,
               "chemin disque non sûr")
        p = ROOT / path
        G._req(not any(x.is_symlink() for x in (p, *p.parents)), "lien symbolique interdit : " + path)
        if p.is_file():
            files[path] = p.read_bytes()

    for path in (G.PLAN, G.STATUS, G.TETRADE, G.NOVO_PLAN, G.NOVO_STATUS, 'chapters.json',
                 'nosology/integrity.json', P.RECEIPT, P.AUTHORITY):
        read(path)
    if P.RECEIPT in files:
        receipt = json.loads(files[P.RECEIPT])
        G._req(isinstance(receipt, dict) and isinstance(receipt.get('courses'), list), 'reçu de publication invalide')
        for course in receipt['courses']:
            G._req(isinstance(course, dict) and course.get('fragment_id') in P.FRAGMENTS and
                   isinstance(course.get('files'), dict), 'cours publié invalide')
            read('nosology/fragments/' + course['fragment_id'] + '.json')
            for path in course['files']:
                read(path)
    # This reads real provenance commits through the same public validator as
    # espace. A catalogue flag alone never creates an adoption exemption.
    adopted = P.adopted_codes(_Tree(files))
    missions, groups = G._novo_missions(plan, status)
    if set(cibles) - set(missions):
        raise G.BettaError("Codes absents du plan Novo_12 : " + " ".join(sorted(set(cibles) - set(missions))))
    ready = {c for n in groups for c in groups[n]
             if G._state(status['cycles'][str(n)]['lessons'][c]) == 'LIVRE' and c not in adopted}
    selected = set(cibles) - adopted if cibles else ready
    if not selected:
        return None
    G._req(selected <= ready, "sélection Novo_12 contenant une leçon non LIVRE")
    numbers = {missions[c][0] for c in selected}
    G._req(len(numbers) == 1, "sélection Novo_12 couvrant plusieurs cycles")
    n = next(iter(numbers))
    G._req(selected == set(groups[n]) - adopted,
           "sélection Novo_12 partielle : prendre toutes les nouvelles leçons déclarées du cycle")
    order = [code for code in groups[n] if code in selected]
    G._req('nosology/integrity.json' in files and (ROOT / 'chapters').is_dir() and (ROOT / 'glossary').is_dir(),
           "infrastructure canonique ou intégrité absente")
    integrity = json.loads(files['nosology/integrity.json'])
    G._req(isinstance(integrity, dict), "registre d'intégrité invalide")
    for code, (number, lesson) in missions.items():
        st = status['cycles'][str(number)]['lessons'][code]
        if G._state(st) != 'INJECTE' and code not in selected:
            continue
        directory = st.get('dir') if G._state(st) == 'INJECTE' else f"livraisons/Livraison Claude/{lesson['label']}/novo12/CYCLE_{number}_{code}"
        G._req(isinstance(directory, str) and directory.startswith('livraisons/Livraison Claude/') and
               directory.endswith(f'/novo12/CYCLE_{number}_{code}') and '..' not in directory.split('/') and
               '\\' not in directory, f"{code} : dossier Novo_12 hors mission")
        G._req(st.get('dir') == directory, f"{code} : dossier Novo_12 hors mission")
        source = ROOT / directory
        G._req(source.is_dir() and not any(x.is_symlink() for x in (source, *source.parents)),
               f"{code} : dossier absent ou lien symbolique")
        for p in source.rglob('*'):
            G._req(not p.is_symlink(), f"{code} : source liée interdite")
            if p.is_file():
                read(p.relative_to(ROOT).as_posix())
        for path in (st.get('canonical') or {}):
            read(path)
        # Existing targets are snapshotted so the guard cannot miss collisions.
        if code in selected:
            G._req(not (ROOT / 'chapters' / code).exists() and not (ROOT / 'chapters' / code).is_symlink() and
                   not (ROOT / 'glossary' / (code.lower() + '.py')).exists() and
                   not (ROOT / 'glossary' / (code.lower() + '.py')).is_symlink(), f"{code} : cible canonique déjà présente")
    proposed = dict(files)
    updated = copy.deepcopy(status)
    catalog = copy.deepcopy(rows)
    targets = {}
    for code in order:
        number, lesson = missions[code]
        st = updated['cycles'][str(number)]['lessons'][code]
        source_files = st.get('files')
        G._req(isinstance(source_files, dict) and source_files, f"{code} : manifeste absent")
        directory = st['dir']
        canonical = {p[len(directory) + 1:]: h for p, h in source_files.items()
                     if p.startswith(directory + '/') and G.managed(p[len(directory) + 1:], {code})}
        for path in canonical:
            source_path = directory + '/' + path
            G._req(source_path in files, f"{code} : source absente : {path}")
            targets[path] = proposed[path] = files[source_path]
        st.update(state='INJECTE', canonical=canonical)
        catalog.append({'code': code, 'covers': [code], 'title': lesson['title'], 'integrated': True,
                        'owner': lesson['fragment'], 'wave': WAVE.get(lesson['fragment']), 'production_cycle': number,
                        'novo12': True, 'provisional_injection': True,
                        'audit_status': 'audit_differe_non_effectue', 'added': date.today().isoformat()})
    updated['cycles'][str(n)]['state'] = ('INJECTE' if all(G._state(row) == 'INJECTE'
        for row in updated['cycles'][str(n)]['lessons'].values()) else 'EN_COURS')
    metadata = {
        G.NOVO_STATUS: json.dumps(updated, ensure_ascii=False, indent=2).encode(),
        'chapters.json': (json.dumps(catalog, ensure_ascii=False, indent=2) + '\n').encode(),
    }
    integrity['chapters.json'] = hashlib.sha256(metadata['chapters.json']).hexdigest()
    metadata['nosology/integrity.json'] = (json.dumps(integrity, ensure_ascii=False, separators=(',', ':')) + '\n').encode()
    proposed.update(metadata)
    P.adopted_codes(_Tree(proposed))
    G.validate(_Tree(files), _Tree(proposed), publication_in_state_codes=adopted)
    return order, targets, metadata, {path: files[path] for path in metadata}, files


def _novo_commit(prepared):
    """Commit under a cooperative local lock, preserving conflicting paths.

    New files use no-clobber links. Metadata is captured before installation,
    checked again, and installed without replacing a concurrent path. Recovery
    also captures before checking; a check followed by os.replace/unlink could
    destroy an intervening edit. Conflicting backups are kept for reconciliation.
    Readers can observe intermediate files. This is neither crash atomic nor a
    distributed transaction; writers holding old descriptors must also cooperate.
    """
    order, targets, metadata, originals, snapshot = prepared
    lock = os.open(ROOT, os.O_RDONLY | os.O_DIRECTORY)
    try:
        # All Novo injectors in this working directory use the same inode lock.
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        _novo_commit_locked(order, targets, metadata, originals, snapshot)
    finally:
        os.close(lock)


def _novo_commit_locked(order, targets, metadata, originals, snapshot):
    stage = Path(tempfile.mkdtemp(prefix='.novo-injection-', dir=ROOT))
    keep_recovery = False
    added, directories, backups, installed = [], [], {}, []
    preserved = []

    def matches(path, raw):
        try:
            return path.is_file() and not path.is_symlink() and path.read_bytes() == raw
        except OSError:
            return False

    def restore(backup, path):
        # The path may have been created again after capture. Never overwrite it.
        try:
            os.link(backup, ROOT / path, follow_symlinks=False)
        except OSError:
            preserved.append(path)

    try:
        for path, raw in {**targets, **metadata}.items():
            p = stage / 'new' / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(raw)
        if any(any(p.is_symlink() for p in (ROOT / path, *(ROOT / path).parents)) or
               not matches(ROOT / path, raw) for path, raw in snapshot.items()):
            raise RuntimeError('Sources ou métadonnées modifiées pendant la préparation : rien injecté')
        for code in order:
            if any(p.exists() or p.is_symlink() for p in (ROOT / 'chapters' / code, ROOT / 'glossary' / (code.lower() + '.py'))):
                raise RuntimeError(code + ' : cible créée pendant la préparation : rien injecté')
        keep_recovery = True
        try:
            for code in order:
                directory = ROOT / 'chapters' / code
                directory.mkdir()  # Atomic reservation; never replace an empty concurrent directory.
                directories.append(directory)
            for path in targets:
                p = ROOT / path
                missing = []
                parent = p.parent
                while not parent.exists():
                    missing.append(parent)
                    parent = parent.parent
                for parent in reversed(missing):
                    parent.mkdir()
                    directories.append(parent)
                os.link(stage / 'new' / path, p)
                added.append(path)
            for index, (path, raw) in enumerate(metadata.items()):
                backup = stage / ('original-' + str(index))
                os.rename(ROOT / path, backup)
                backups[path] = backup
                if not matches(backup, originals[path]):
                    raise RuntimeError('Métadonnées modifiées pendant l’injection : ' + path)
                os.link(stage / 'new' / path, ROOT / path)
                installed.append(path)
            keep_recovery = False
        except BaseException as error:
            for index, (path, backup) in enumerate(reversed(list(backups.items()))):
                if path in installed:
                    captured = stage / ('rollback-metadata-' + str(index))
                    try:
                        os.rename(ROOT / path, captured)
                    except FileNotFoundError:
                        pass
                    except OSError:
                        preserved.append(path)
                        continue
                    else:
                        if not matches(captured, metadata[path]):
                            restore(captured, path)
                            preserved.append(path)
                            continue
                restore(backup, path)
            for index, path in enumerate(reversed(added)):
                captured = stage / ('rollback-source-' + str(index))
                try:
                    os.rename(ROOT / path, captured)
                except FileNotFoundError:
                    continue
                except OSError:
                    preserved.append(path)
                    continue
                if not matches(captured, targets[path]):
                    restore(captured, path)
                    preserved.append(path)
            for directory in reversed(directories):
                try:
                    directory.rmdir()
                except FileNotFoundError:
                    pass
                except OSError:
                    preserved.append(directory.relative_to(ROOT).as_posix())
            if preserved:
                keep_recovery = True
                raise RuntimeError('Échec d’injection ; travail concurrent préservé, réconciliation requise : ' +
                                   ', '.join(sorted(set(preserved))) + '; sauvegardes : ' + str(stage)) from error
            keep_recovery = False
            raise
    finally:
        if not keep_recovery:
            shutil.rmtree(stage)


def inject_novo(cibles, plan, status, rows):
    try:
        prepared = _novo_prepare(cibles, plan, status, rows)
    except (ValueError, OSError) as error:
        sys.exit("Injection Novo_12 refusée, rien n'a été copié :\n" + str(error))
    if prepared is None:
        print('0 leçons Novo_12 injectées : aucune leçon LIVRE')
        return
    _novo_commit(prepared)
    print(f"{len(prepared[0])} leçons Novo_12 injectées : {' '.join(prepared[0])}")


def main(cibles, novo=False):
    plan_rel, status_rel, flag = (("organisation/progression/plan-novo12.json", "organisation/novo12_status.json", "novo12") if novo
                                  else ("organisation/progression/plan-betta-cycles.json", "organisation/betta_status.json", "betta"))
    plan = charger(plan_rel)
    status = charger(status_rel)
    rows = charger("chapters.json")
    if novo:
        return inject_novo(cibles, plan, status, rows)
    transferred = {code for cycle in status['cycles'].values() if cycle.get('state') == 'TRANSFERE_NOVO12'
                   for code in cycle['lessons']}
    transferred_ready = {code for cycle in status['cycles'].values() if cycle.get('state') == 'TRANSFERE_NOVO12'
                         for code, st in cycle['lessons'].items() if isinstance(st, dict) and st.get('state') == 'LIVRE'}
    if transferred.intersection(cibles) or transferred_ready.intersection(cibles or transferred_ready):
        sys.exit('Injection Betta refusée : missions transférées à Novo_12 ; utiliser --novo et le nouveau plan')
    lecons = {l["code"]: (c["number"], l) for c in plan["cycles"] for a in c["agents"] for l in a["lessons"]}
    existants, faits = {r["code"] for r in rows}, []
    # Contrôle préalable (constats Codex PR 96) : tous les fichiers présents et, pour Novo_12,
    # porte de vérité VÉRITÉ OK, avant toute copie canonique.
    sys.path.insert(0, str(ROOT / "tools"))
    try:
        from tools.betta_verite import controler
    except ModuleNotFoundError:
        from betta_verite import controler
    erreurs = []
    for n, cyc in status["cycles"].items():
        for code, st in cyc["lessons"].items():
            if not isinstance(st, dict) or st.get("state") != "LIVRE" or (cibles and code not in cibles):
                continue
            src = ROOT / st["dir"]
            for f in [src / "chapters" / code / f"{code}_{x}.html" for x in "abcd"] + [src / "glossary" / f"{code.lower()}.py", src / "rapport.md"]:
                if not f.is_file():
                    erreurs.append(f"{code} : fichier manquant {f.relative_to(ROOT)}")
            if code in existants or (ROOT / "chapters" / code).exists():
                erreurs.append(f"{code} : déjà présent dans chapters/ ou chapters.json")
            if novo:
                erreurs += [f"{code} : vérité — {e}" for e in controler(src)]
    if erreurs:
        sys.exit("Injection refusée, rien n'a été copié :\n" + "\n".join(erreurs))
    for n, cyc in status["cycles"].items():
        for code, st in cyc["lessons"].items():
            if not isinstance(st, dict) or st.get("state") != "LIVRE" or (cibles and code not in cibles):
                continue
            src = ROOT / st["dir"]
            dst_ch, gl = ROOT / "chapters" / code, src / "glossary" / f"{code.lower()}.py"
            if dst_ch.exists() or code in existants:
                sys.exit(f"{code} : déjà présent dans chapters/ ou chapters.json — arrêt")
            shutil.copytree(src / "chapters" / code, dst_ch)
            shutil.copy2(gl, ROOT / "glossary" / gl.name)
            canon = {str(p.relative_to(ROOT)): sha(p) for p in sorted(dst_ch.rglob("*")) if p.is_file()}
            canon[f"glossary/{gl.name}"] = sha(ROOT / "glossary" / gl.name)
            st.update(state="INJECTE", canonical=canon)
            cycle, l = lecons[code]
            assert cycle == int(n), f"{code} : cycle incohérent"
            rows.append({"code": code, "covers": [code], "title": l["title"], "integrated": True,
                         "owner": l["fragment"], "wave": WAVE.get(l["fragment"]), "production_cycle": cycle,
                         flag: True, "provisional_injection": True,
                         "audit_status": "audit_differe_non_effectue", "added": date.today().isoformat()})
            faits.append(code)
        if all(isinstance(v, dict) and v.get("state") == "INJECTE" for v in cyc["lessons"].values()):
            cyc["state"] = "INJECTE"
    ecrire(status_rel, status, nl=False)
    ecrire("chapters.json", rows)
    integ = charger("nosology/integrity.json")
    integ["chapters.json"] = sha(ROOT / "chapters.json")
    ecrire("nosology/integrity.json", integ, compact=True)
    print(f"{len(faits)} leçons injectées : {' '.join(faits)}")


if __name__ == "__main__":
    main(set(a for a in sys.argv[1:] if a != "--novo"), novo="--novo" in sys.argv)
