#!/usr/bin/env python3
"""Espace partagé MEDINA : dépôt, audit sur place, injection après audit croisé.
  python3 tools/espace.py deposer  <dossier_lot> --auteur Claude|Codex
  python3 tools/espace.py ouvrir   <CODE>          # copie de travail de main pour corriger sur place
  python3 tools/espace.py auditer  <CODE> --auditeur Claude|Codex --verdict favorable|favorable_sous_reserves_mineures|defavorable --rapport "<texte ou lien>"
  python3 tools/espace.py injecter <CODE>
  python3 tools/espace.py garde <avant> <apres>    # CI
"""
import argparse, hashlib, json, os, pathlib, shutil, subprocess, sys
R = pathlib.Path(__file__).resolve().parents[1]
W = R.parent / "medina_espace"
ESP = {"Claude": "espace_partage/COURS_CLAUDE_A_AUDITER_PAR_CODEX", "Codex": "espace_partage/COURS_CODEX_A_AUDITER_PAR_CLAUDE"}
OK = {"favorable", "favorable_sous_reserves_mineures"}
CANON = ("chapters/", "glossary/", "chapters.json")

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
    lot = pathlib.Path(lot).resolve(); m = json.loads((lot / "livraison.json").read_text())
    code = m["chapters"][0]["code"]; main_frais(); d = W / ESP[auteur] / code
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
    main_frais(); d, auteur = dossier(code)
    if auditeur == auteur: sys.exit("REFUS : l'auteur ne peut pas auditer son propre cours.")
    e = json.loads((d / "ETAT.json").read_text()); e["fichiers"] = empreintes(d)
    e["audits"].append({"auditeur": auditeur, "verdict": verdict, "rapport": rapport, "fichiers": e["fichiers"]})
    e["statut"] = "audite_favorable" if verdict in OK else "a_corriger"
    (d / "ETAT.json").write_text(json.dumps(e, ensure_ascii=False, indent=1) + "\n")
    pousser(f"Espace partagé : {auditeur} audite {code} ({verdict})", str(d.relative_to(W)))

def injecter(code):
    main_frais(); d, auteur = dossier(code); e = json.loads((d / "ETAT.json").read_text()); f = empreintes(d)
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
    etats = []
    for base in ESP.values():
        for p in subprocess.run(["git", "ls-tree", "-r", "--name-only", ap, base], cwd=R, capture_output=True, text=True).stdout.split():
            if p.endswith("/ETAT.json"):
                e = json.loads(subprocess.run(["git", "show", f"{ap}:{p}"], cwd=R, capture_output=True, text=True).stdout)
                etats += [x["fichiers"] for x in e["audits"] if x["auditeur"] != e["auteur"] and x["verdict"] in OK]
    err = []
    for p in subprocess.run(["git", "diff", "--name-only", f"{av}..{ap}"], cwd=R, capture_output=True, text=True).stdout.split():
        if not p.startswith(CANON): continue
        b = subprocess.run(["git", "show", f"{ap}:{p}"], cwd=R, capture_output=True).stdout
        if b and not any(x.get(p) == hashlib.sha256(b).hexdigest() for x in etats): err.append(p)
    print("Sources canoniques modifiées sans audit croisé :", err or "aucune"); return 1 if err else 0

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["garde"]: sys.exit(garde(a[1], a[2]))
    p = argparse.ArgumentParser(); p.add_argument("action"); p.add_argument("cible")
    p.add_argument("--auteur"); p.add_argument("--auditeur"); p.add_argument("--verdict"); p.add_argument("--rapport", default="")
    x = p.parse_args(a)
    {"deposer": lambda: deposer(x.cible, x.auteur), "ouvrir": lambda: (main_frais(), print(W / dossier(x.cible)[0].relative_to(W))),
     "auditer": lambda: auditer(x.cible, x.auditeur, x.verdict, x.rapport), "injecter": lambda: injecter(x.cible)}[x.action]()
