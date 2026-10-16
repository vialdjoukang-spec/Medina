#!/usr/bin/env python3
"""Contrôle d'application des propositions sur une COPIE du worktree (jamais sur les sources canoniques).

Usage : python3 propositions/appliquer_copie.py <racine du worktree> <dossier de copie vide>
Applique : corrections.py (43 remplacements), G99_c_semio.html (bouton + discipline en tête de #pS),
G99_pop1_semio.html (fin de G99_pop1.html), G99_pop2_attr.html (fin de G99_pop2.html),
G99_c_sciences.html (figures 3 et 4 remplacées, encadrés « Corrélation clinique » remplacés, ajouts),
puis lance `python3 test_v7.py --static G99` dans la copie et imprime le résultat.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import corrections  # noqa: E402


def sans_commentaires(t):
    return re.sub(r"<!--.*?-->", "", t, flags=re.S).strip()


def main():
    src, dst = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".git", "docs", "livraisons", "*.zip", "*.pdf"), dirs_exist_ok=True)
    ch = dst / "chapters/G99"
    # 1. remplacements locaux
    for e in corrections.P:
        f = dst / e["fichier"]
        t = f.read_text(encoding="utf-8")
        assert t.count(e["ancien"]) == 1, e["id"]
        f.write_text(t.replace(e["ancien"], e["nouveau"], 1), encoding="utf-8")
    # 2. sémiologie en tête de #pS
    semio = sans_commentaires((ICI / "G99_c_semio.html").read_text(encoding="utf-8"))
    bouton, discipline = semio.split("\n", 1)
    c = (ch / "G99_c.html").read_text(encoding="utf-8")
    c = c.replace('<button role="tab" aria-selected="true" aria-controls="g99-s-anat"', '<button role="tab" aria-selected="false" aria-controls="g99-s-anat"', 1)
    c = c.replace('<div class="sci-bar ui" role="tablist">', '<div class="sci-bar ui" role="tablist">' + bouton.strip(), 1)
    c = c.replace('<div class="chap-body sci-body"><div class="sci" id="g99-s-anat">', '<div class="chap-body sci-body">' + discipline.strip() + '<div class="sci" id="g99-s-anat" hidden>', 1)
    # 3. sciences : figures et encadrés
    sci = (ICI / "G99_c_sciences.html").read_text(encoding="utf-8")
    blocs = re.split(r"<!-- ===== (g99-s-\w+) : .*?===== -->", sci)
    parts = {blocs[i]: sans_commentaires(blocs[i + 1]) for i in range(1, len(blocs), 2)}
    for disc, contenu in parts.items():
        m = re.search(r'(<div class="sci" id="%s"[^>]*>)(.*?)(</section></div>)' % disc, c, flags=re.S)
        assert m, disc
        corps = m.group(2)
        figs = re.findall(r"<figure>.*?</figure>", contenu, flags=re.S)
        reste = re.sub(r"<figure>.*?</figure>", "", contenu, flags=re.S).strip()
        if disc in ("g99-s-anat", "g99-s-histo"):
            corps = re.sub(r"<figure>.*?</figure>", figs[0], corps, count=1, flags=re.S)
        elif figs:
            corps = corps.replace("<div class=\"key\"><b>Corrélation clinique.</b>", figs[0] + "\n<div class=\"key\"><b>Corrélation clinique.</b>", 1)
        corps = re.sub(r'<div class="key"><b>Corrélation clinique\.</b>.*?</div>', reste.replace("\\", "\\\\"), corps, count=1, flags=re.S)
        c = c[:m.start(2)] + corps + c[m.end(2):]
    (ch / "G99_c.html").write_text(c, encoding="utf-8")
    # 4. fenêtres
    for nom, cible in (("G99_pop1_semio.html", "G99_pop1.html"), ("G99_pop2_attr.html", "G99_pop2.html")):
        f = ch / cible
        f.write_text(f.read_text(encoding="utf-8").rstrip() + "\n" + sans_commentaires((ICI / nom).read_text(encoding="utf-8")) + "\n", encoding="utf-8")
    # 4 bis. glossaire : sous-codes CIM cités par la proposition P02
    g = dst / "glossary/g99.py"
    g.write_text(g.read_text(encoding="utf-8").rstrip() + "\n" + (ICI / "glossary_g99_ajouts.py").read_text(encoding="utf-8"), encoding="utf-8")
    # 5. marqueurs d'audit retirés (ils ne font pas partie du contrat HTML)
    for f in list(ch.glob("*.html")):
        f.write_text(re.sub(r"\s?\[S\d+\]", "", f.read_text(encoding="utf-8")), encoding="utf-8")
    r = subprocess.run([sys.executable, "test_v7.py", "--static", "G99"], cwd=dst, capture_output=True, text=True)
    print(r.stdout.strip(), r.stderr.strip()[-2000:])


if __name__ == "__main__":
    main()
