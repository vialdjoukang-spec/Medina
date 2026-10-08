"""Les intitulés affichés ne contiennent plus « autre », « sans précision » ni « non classé ailleurs »."""
import json
import re
import unittest
from pathlib import Path

from tools import libelles

ROOT = Path(__file__).resolve().parents[1]
INTERDIT = re.compile(r"\bautres?\b|sans précision|non class[ée]e?s? ailleurs|non précis", re.I)


def catalogue():
    source = (ROOT / "shell/medina_front.html").read_text(encoding="utf-8")
    data = json.loads(re.search(r'<script id="medora-data" type="application/json">(.*?)</script>', source, re.S).group(1))
    return data["entries"]


class Libelles(unittest.TestCase):
    def test_blocs_et_chapitres_sans_mot_interdit(self):
        fautes = []
        for entry in catalogue():
            for libelle in (libelles.bloc(entry["block"], entry["blockTitle"]),
                            libelles.chapitre(entry["code"], entry["title"])):
                if INTERDIT.search(libelle):
                    fautes.append((entry["code"], libelle))
        self.assertEqual(fautes[:10], [], f"{len(fautes)} intitulés interdits")

    def test_nom_de_categorie_court(self):
        longs = {entry["block"]: libelles.bloc(entry["block"], entry["blockTitle"]) for entry in catalogue()}
        trop = {code: nom for code, nom in longs.items() if len(nom) > 95}
        self.assertEqual(trop, {})

    def test_les_codes_restent_intacts(self):
        self.assertEqual(libelles.chapitre("J12", "Pneumonie virale, non classées ailleurs"), "Pneumonie virale")


if __name__ == "__main__":
    unittest.main()
