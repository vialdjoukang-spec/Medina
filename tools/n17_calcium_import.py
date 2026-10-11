"""Exception documentaire explicite de Vial, pour un produit et N17 seulement.

La garde contrôle les preuves structurées, pas la vérité médicale des passages.
"""
import hashlib
import re
from urllib.parse import urlsplit

AUTHORITY = "docs/collaboration/instructions/N17_CALCIUM_IMPORTE_VIAL_2026-10-11.md"
AUTHORITY_SHA256 = "e1d8a17773db93924e2e014c7750295ff1ae80bd00247d534794de98b0645706"
PRODUCT = "Calciumgluconat B. Braun 10 % Injektionslösung"
PRESENTATIONS = {"Mini-Plasco 10 ml", "Mini-Plasco connect 10 ml"}


def require(condition, message):
    if not condition:
        raise ValueError("Calcium importé N17 : " + message)


def authority(tree):
    raw = tree.read(AUTHORITY)
    require(hashlib.sha256(raw).hexdigest() == AUTHORITY_SHA256,
            "instruction explicite absente ou modifiée")
    return {"path": AUTHORITY, "sha256": AUTHORITY_SHA256}


def source(data, description):
    fields = ("organization", "title", "url", "version_date", "section", "passage", "accessed_on")
    require(isinstance(data, dict) and all(isinstance(data.get(k), str) and data[k].strip() for k in fields),
            description + " : passage primaire localisé requis")
    parsed = urlsplit(data["url"])
    require(parsed.scheme == "https" and bool(parsed.hostname), description + " : URL HTTPS requise")
    require(isinstance(data.get("download_sha256"), str) and
            re.fullmatch(r"[0-9a-f]{64}", data["download_sha256"]),
            description + " : empreinte du document effectivement lu requise")


def validate_product(tree, row, ident, scope, chapter_code):
    """Do not relax the historical whole-fragment or other-product Swiss gate."""
    require((ident, scope, chapter_code, row.get("chapter_code"), row.get("kind")) ==
            ("S04", "chapter", "N17", "N17", "medication"), "périmètre non autorisé")
    data = row.get("imported_product")
    require(isinstance(data, dict), "preuve du produit importé absente")
    require(data.get("authority") == authority(tree), "autorité ciblée non documentée")
    require(data.get("product_name") == PRODUCT and data.get("presentation") in PRESENTATIONS,
            "produit exact ou présentation incorrects")
    require(data.get("country_of_origin") == "DE" and data.get("status") == "import_hospitalier",
            "statut d'import hospitalier allemand non explicite")
    require("swiss_authorization_number" in data and data["swiss_authorization_number"] is None and
            row.get("swissmedic_product") is None, "autorisation Swissmedic fictive ou ambiguë interdite")
    hospital = data.get("swiss_hospital_source")
    source(hospital, "document hospitalier suisse")
    require(hospital.get("country") == "CH", "source hospitalière non identifiée comme suisse")
    info = data.get("professional_information")
    source(info, "information professionnelle du produit exact")
    require(info.get("product_name") == PRODUCT, "information professionnelle d'un autre produit")
    require((info.get("type"), info.get("country")) in {
        ("fachinformation_allemande", "DE"), ("monographie_hospitaliere_suisse", "CH")},
        "seules la FI allemande ou la monographie locale explicitement autorisées sont admissibles")
    require(isinstance(data.get("clinical_arbitration"), str) and data["clinical_arbitration"].strip(),
            "arbitrage clinique et distinction des rôles des sources absents")
    require(isinstance(data.get("indication_status"), str) and data["indication_status"].strip(),
            "statut de l'usage vis-à-vis de la FI non indiqué")
