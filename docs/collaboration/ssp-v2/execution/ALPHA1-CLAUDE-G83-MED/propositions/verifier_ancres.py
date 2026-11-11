#!/usr/bin/env python3
"""Vérifie que chaque « ANCIEN : » des propositions figure exactement une fois dans le fichier canonique visé,
puis applique toutes les propositions sur une copie temporaire (jamais sur le dépôt) pour contrôler test_v7.py --static.

Usage : python3 propositions/verifier_ancres.py <racine du worktree> [<dossier de copie>]
"""
import json, re, shutil, subprocess, sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
RAC = Path(sys.argv[1]).resolve()
CIBLE = {  # proposition -> fichier par défaut
    "G83_d_1.html": "chapters/G83/G83_d.html",
    "G83_b_1.html": "chapters/G83/G83_b.html",
    "G83_mineurs.html": None,
    "G83_enrichissements.html": None,
    "G83_a_semio_clinique.html": "chapters/G83/G83_a.html",
}
BLOC = re.compile(r"ANCIEN : (.*?)\n(?:NOUVEAU : -->\n|NOUVEAU : ci-dessous, bloc \(A\)\.)(.*?)(?=\n<!--|\Z)", re.S)


def fichier_vise(prop, entete, precedent):
    m = re.findall(r"(chapters/G83/G83_[a-z0-9]+\.html)", entete)
    if m:
        return m[-1]
    if "G83_pop2.html" in entete:
        return "chapters/G83/G83_pop2.html"
    if "G83_pop1.html" in entete or "fenêtre g83-sevrage" in entete:
        return "chapters/G83/G83_pop1.html"
    return CIBLE[prop] or precedent


def paires():
    out = []
    for prop in CIBLE:
        t = (ICI / prop).read_text(encoding="utf-8")
        f = None
        for m in BLOC.finditer(t):
            entete = t[max(0, t.rfind("<!--", 0, m.start())):m.start()]
            f = fichier_vise(prop, entete, f)
            nouveau = m.group(2).strip()
            if prop == "G83_a_semio_clinique.html" and "(A)" in m.group(0):
                nouveau = t.split("<!-- (A) -->")[1].split("<!-- (B) -->")[0].strip()
            out.append({"proposition": prop, "fichier": f, "ancien": m.group(1).strip(), "nouveau": nouveau})
    return out


def main():
    ps = paires()
    res = []
    for p in ps:
        n = (RAC / p["fichier"]).read_text(encoding="utf-8").count(p["ancien"])
        res.append({"proposition": p["proposition"], "fichier": p["fichier"], "ancien": p["ancien"][:120], "occurrences": n})
    ok = all(r["occurrences"] == 1 for r in res)
    rapport = {"paires": len(res), "toutes_uniques": ok, "detail": res}
    if len(sys.argv) > 2:
        copie = Path(sys.argv[2]).resolve()
        if copie.exists():
            shutil.rmtree(copie)
        shutil.copytree(RAC, copie, ignore=shutil.ignore_patterns(".git"))
        for p in ps:
            f = copie / p["fichier"]
            t = f.read_text(encoding="utf-8")
            if t.count(p["ancien"]) == 1:
                f.write_text(t.replace(p["ancien"], p["nouveau"]), encoding="utf-8")
        # Sémiologie : bouton et panneau en tête de pS ; carte clinique dans g83-5 ; fenêtres en fin de pop1
        c = copie / "chapters/G83/G83_c.html"
        sem = (ICI / "G83_c_semio.html").read_text(encoding="utf-8")
        bouton = re.search(r"<!-- \(1\) barre -->\n(.*?)\n", sem).group(1)
        panneau = sem.split("<!-- (2) corps -->")[1].strip()
        t = c.read_text(encoding="utf-8")
        t = t.replace('<button role="tab" aria-selected="true" aria-controls="g83-s-anat"', bouton + '<button role="tab" aria-selected="false" aria-controls="g83-s-anat"', 1)
        t = t.replace('<div class="chap-body sci-body"><div class="sci" id="g83-s-anat">', '<div class="chap-body sci-body">' + panneau + '<div class="sci" id="g83-s-anat" hidden>', 1)
        c.write_text(t, encoding="utf-8")
        a = copie / "chapters/G83/G83_a.html"
        clin = (ICI / "G83_a_semio_clinique.html").read_text(encoding="utf-8").split("<!-- (B) -->")[1].strip()
        t = a.read_text(encoding="utf-8")
        cle = '<div class="key"><b>À retenir.</b> Rechercher la rétention'
        assert t.count(cle) == 1
        a.write_text(t.replace(cle, clin + "\n" + cle), encoding="utf-8")
        p1 = copie / "chapters/G83/G83_pop1.html"
        fen = (ICI / "G83_pop1_semio.html").read_text(encoding="utf-8")
        fen = re.sub(r"<!--.*?-->\n?", "", fen, flags=re.S)
        p1.write_text(p1.read_text(encoding="utf-8") + fen, encoding="utf-8")
        # Les marqueurs [Sx] de traçabilité de l'audit sont retirés à l'intégration (leur lien vit dans p.src) : retrait sur la copie.
        for f in (copie / "chapters/G83").glob("*.html"):
            f.write_text(re.sub(r"\s?\[S\d+(?: ; S\d+)*\]", "", f.read_text(encoding="utf-8")), encoding="utf-8")
        r = subprocess.run([sys.executable, "test_v7.py", "--static", "G83"], cwd=copie, capture_output=True, text=True, timeout=600)
        rapport["test_v7_static_apres_application"] = (r.stdout + r.stderr).strip()[-600:]
    print(json.dumps(rapport, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
