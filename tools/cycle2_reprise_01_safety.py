#!/usr/bin/env python3
"""Corrections ciblées des remises du Cycle 2, sans injection ni audit inventé.

Les passes 1 et preuves des auteurs restent immuables. Cette migration ne
transforme aucune réserve en verdict favorable. Les labels suisses du produit
exact ont été lus lors de la reprise; le reçu sépare corrections et audits.
"""
from __future__ import annotations
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / 'docs/collaboration/reprises/2026-10-14/01-safety.json'
BASES = {c: next(ROOT.glob('livraisons/Livraison Codex/*/travail/CYCLE_02_' + c)) for c in ('G45', 'E10', 'N18', 'D64')}
FILES: dict[Path, str] = {}
OPS: list[dict] = []

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def path(code: str, suffix: str) -> Path:
    return BASES[code] / f'chapters/{code}/{code}_{suffix}.html'

def segment(text: str, scope: str | None) -> tuple[int, int]:
    if scope is None:
        return 0, len(text)
    kind, key = scope.split(':', 1)
    if kind == 'template':
        pattern = r'<template\b[^>]*\bdata-pop="' + re.escape(key) + r'"[^>]*>.*?</template>'
    elif kind == 'part':
        pattern = r'<h3\b[^>]*\bid="' + re.escape(key) + r'"[^>]*>.*?(?=<h3\b|</section>)'
    else:
        raise ValueError(scope)
    matches = list(re.finditer(pattern, text, re.S))
    if len(matches) != 1:
        raise ValueError(f'Scope absent ou ambigu: {scope}')
    return matches[0].span()

def edit(code: str, suffix: str, old: str, new: str, scope: str | None = None, reason: str = '') -> None:
    p = path(code, suffix)
    text = FILES.get(p, p.read_text(encoding='utf-8'))
    a, b = segment(text, scope)
    local = text[a:b]
    if local.count(old) != 1:
        raise ValueError(f'Correction non univoque: {code}/{suffix}/{scope}: {old[:70]}')
    FILES[p] = text[:a] + local.replace(old, new, 1) + text[b:]
    OPS.append({'code': code, 'path': p.relative_to(ROOT).as_posix(), 'scope': scope, 'reason': reason, 'before': old, 'after': new})

def add_window(code: str, suffix: str, key: str, html: str, reason: str) -> None:
    edit(code, suffix, '<p class="src">', html + '<p class="src">', 'template:' + key, reason)

def add_part(code: str, suffix: str, key: str, html: str, reason: str) -> None:
    p = path(code, suffix)
    text = FILES.get(p, p.read_text(encoding='utf-8'))
    a, b = segment(text, 'part:' + key)
    block = text[a:b]
    footer = re.search(r'<(?:div class="(?:key|quiz)|p class="src")', block)
    i = footer.start() if footer else len(block)
    edit(code, suffix, block, block[:i] + html + block[i:], 'part:' + key, reason)

def main() -> None:
    if RECEIPT.exists():
        print('Migration 01 déjà enregistrée; reçu historique conservé, pas de réapplication.')
        return
    inputs_path = ROOT / 'organisation/execution-20261014/cross-inputs.json'
    inputs = json.loads(inputs_path.read_text(encoding='utf-8'))
    originals = {}
    for item in inputs['inputs']:
        for rel, expected in item['files'].items():
            p = BASES[item['code']] / rel
            if sha(p.read_bytes()) != expected:
                raise SystemExit(f'Entrée modifiée depuis la passe 1: {p}')
            originals[p.relative_to(ROOT).as_posix()] = expected

    edit('G45', 'pop2', 'insuffisance hépatique sévère et troisième trimestre de grossesse.', 'insuffisance hépatique sévère et troisième trimestre de grossesse. Pour ce produit précis, la maladie de Crohn et la colite ulcéreuse, maladies inflammatoires intestinales, ainsi que l’insuffisance cardiaque sévère de classe NYHA III–IV sont également des contre-indications.', 'template:g45-aspirine', 'G45-R1: exclusions exactes Aspirine Cardio')
    edit('G45', 'd', "ou d'insuffisance rénale sévère définie dans sa fiche par une clairance inférieure à 30 mL/min.", "ou d'insuffisance rénale sévère définie dans sa fiche par une clairance inférieure à 30 mL/min. Sa fiche exclut aussi la maladie de Crohn, la colite ulcéreuse et l’insuffisance cardiaque sévère NYHA III–IV.", 'part:g45-p02-partie-2', 'G45-R1: concordance du corps')
    edit('G45', 'pop2', 'Maladie hépatique active, élévation persistante inexpliquée des transaminases, myopathie, grossesse et allaitement figurent parmi les exclusions.', 'Sortis est contre-indiqué en cas de maladie hépatique active, de cholestase ou de myopathie. Une élévation persistante et inexpliquée des transaminases à plus de trois fois la limite supérieure normale l’exclut également. Son utilisation est aussi contre-indiquée pendant la grossesse et l’allaitement. La cholestase est un trouble de l’écoulement de la bile. L’association au glécaprévir/pibrentasvir, traitement antiviral de l’hépatite C, est également contre-indiquée.', 'template:g45-sortis', 'G45-R2: cholestase et association antivirale')
    edit('G45', 'pop2', 'Des douleurs ou une faiblesse musculaires appellent une évaluation et des enzymes musculaires selon le contexte.', 'Des douleurs ou une faiblesse musculaires appellent une évaluation. Une myopathie suspectée ou diagnostiquée, ou une élévation significative de la créatine phosphokinase (CPK), impose l’arrêt immédiat de Sortis selon sa fiche. La CPK est une enzyme dont l’élévation peut signaler une lésion musculaire; une myalgie isolée ne suffit pas à définir une myopathie. La fiche ne fournit pas ici de seuil chiffré unique pour cet arrêt.', 'template:g45-sortis', 'G45-R2: conduite explicite et CPK')
    edit('G45', 'd', 'de maladie hépatique active, de myopathie et de grossesse.', 'de maladie hépatique active, de cholestase, de myopathie, de grossesse et d’association au glécaprévir/pibrentasvir.', 'part:g45-p02-partie-2', 'G45-R2: concordance des exclusions')
    add_part('G45', 'd', 'g45-p02-partie-3', '<div class="alert"><b>Arrêt et évaluation urgente.</b> Une hémorragie majeure sous Eliquis impose son arrêt. Une myopathie suspectée ou diagnostiquée, ou une élévation significative de CPK sous Sortis, impose aussi l’arrêt immédiat du produit. Les <button class="w" data-k="g45-eliquis">précautions de l’apixaban (hémorragie et situations non recommandées)</button> et la <button class="w" data-k="g45-sortis">toxicité musculaire (distinction avec une myalgie)</button> sont détaillées dans leurs fiches.</div>', 'G45-R2/R3: alerte dans le corps')
    add_window('G45', 'pop2', 'g45-eliquis', '<p>Une hémorragie majeure impose l’arrêt d’Eliquis et une prise en charge urgente adaptée; cette fenêtre ne prescrit pas de protocole de réversion. Chez une personne ayant un syndrome des antiphospholipides et un antécédent de thrombose, l’apixaban n’est pas recommandé, particulièrement en cas de triple positivité: anticoagulant lupique, anticorps anticardiolipine et anti-bêta-2-glycoprotéine I. Il s’agit d’une situation non recommandée dans la fiche, distincte de ses contre-indications formelles.</p>', 'G45-R3: antiphospholipides et hémorragie majeure')
    add_part('G45', 'd', 'g45-p02-partie-2', '<p>Le syndrome des antiphospholipides avec antécédent thrombotique relève d’une <button class="w" data-k="g45-eliquis">utilisation non recommandée de l’apixaban (population et triple positivité)</button>, et non d’une contre-indication formelle ajoutée à tort à la fiche.</p>', 'G45-R3: distinction réglementaire')
    add_window('E10', 'pop2', 'e10-p02-fenetre-1', '<p>Les interactions du glucagon imposent une surveillance ciblée: l’indométacine peut supprimer sa réponse hyperglycémiante, voire provoquer une hypoglycémie; l’effet anticoagulant de la warfarine peut augmenter; sous bêtabloquant, le pouls et la pression artérielle peuvent s’élever transitoirement. Ces interactions ne sont pas les contre-indications de Baqsimi et ne justifient pas de retarder les secours devant une hypoglycémie sévère.</p>', 'E10-R03: trois interactions Baqsimi')
    add_part('E10', 'd', 'e10-p02-partie-2', '<div class="alert"><b>Interactions du secours.</b> Le <button class="w" data-k="e10-p02-fenetre-1">glucagon nasal (indométacine, warfarine et bêtabloquants)</button> exige une surveillance de la réponse et des effets associés. Une interaction ne devient pas une contre-indication supplémentaire et ne retarde pas l’alerte urgente.</div>', 'E10-R03: lien et alerte dans la pharmacologie')
    edit('N18', 'pop2', 'La dose initiale est 20 mg une fois par jour.', 'La dose initiale est 20 mg une fois par jour, sauf en cas de traitement déjà associé à un inhibiteur modéré du CYP3A4: elle est alors de 10 mg une fois par jour.', 'template:n18-kerendia', 'N18-R01: exception dans la cellule de dose')
    edit('N18', 'pop2', 'Les inhibiteurs puissants du CYP3A4 et la maladie d’Addison sont des contre-indications.', 'Les inhibiteurs puissants du CYP3A4 et la maladie d’Addison sont des contre-indications. Chez un patient recevant déjà un inhibiteur modéré, notamment érythromycine ou vérapamil, Kerendia débute à 10 mg une fois par jour, même si le DFGe est d’au moins 60 mL/min/1,73 m². Le potassium est surveillé lors de l’instauration et des changements de dose de ces traitements associés.', 'template:n18-kerendia', 'N18-R01: interaction et contrôle associé')
    add_part('N18', 'd', 'n18-p01-partie-3', '<p>L’initiation de <button class="w" data-k="n18-kerendia">Kerendia (exception liée au CYP3A4)</button> ne dépend pas du seul DFGe: un inhibiteur modéré déjà prescrit impose une dose initiale de 10 mg par jour et une surveillance du potassium liée au traitement associé.</p>', 'N18-R01: concordance pharmacologie')
    edit('D64', 'd', '300 mg ; anémie iatrogène', '300 mg ; prévention ou traitement d’une carence iatrogène en pyridoxine lors de l’administration d’un antagoniste de cette vitamine', 'part:d64-p01-partie-4', 'D64-R02: indication de 150 mg corrigée')
    edit('D64', 'd', 'La cause médicamenteuse et les contre-indications doivent être examinées.', 'Ce schéma ne traite pas toute anémie médicamenteuse et ne corrige pas une myélotoxicité non liée à cette carence.', 'part:d64-p01-partie-4', 'D64-R02: limite explicite')
    add_window('D64', 'pop2', 'd64-p01-w1', '<p>La dose de 150 mg par jour concerne notamment la prévention ou le traitement d’une carence provoquée par un antagoniste de la pyridoxine; elle ne vaut pas pour toute anémie iatrogène. Benadon est contre-indiqué en cas d’hypersensibilité à la pyridoxine ou à ses excipients, de grossesse, d’allaitement, d’insuffisance hépatique ou rénale et avant 12 ans; il n’est pas recommandé entre 12 et 15 ans.</p><p>Il peut diminuer l’effet de la phénytoïne, du phénobarbital et de l’altrétamine et augmenter la photosensibilité liée à l’amiodarone. L’interaction avec la lévodopa ne se produit pas lorsque celle-ci est associée à un inhibiteur périphérique de la décarboxylase.</p>', 'D64-R02/R03: population, hypersensibilité et interactions Benadon')

    for p, text in FILES.items():
        original = p.read_text(encoding='utf-8')
        if re.findall(r'<h3\b[^>]*\bid="([^"]+)"', original) != re.findall(r'<h3\b[^>]*\bid="([^"]+)"', text):
            raise SystemExit(f'Contrat des sous-parties modifié: {p}')
        if re.findall(r'<template\b[^>]*\bdata-pop="([^"]+)"', original) != re.findall(r'<template\b[^>]*\bdata-pop="([^"]+)"', text):
            raise SystemExit(f'Contrat des fenêtres modifié: {p}')
    for p, text in FILES.items():
        p.write_text(text, encoding='utf-8')
    final_files = {rel: sha((ROOT / rel).read_bytes()) for rel in originals}
    receipt = {
        'schema_version': 1, 'cycle': 2, 'actor': 'ChatGPT coordinateur, corrections ciblées',
        'applied_at': datetime.now(timezone.utc).isoformat(),
        'status': 'corrections_ciblees_soumises_a_relecture',
        'canonical_injection': False, 'cross_audit_completed': False,
        'counter_audit_completed': False, 'medical_human_validation': False,
        'original_input': {'path': inputs_path.relative_to(ROOT).as_posix(), 'sha256': sha(inputs_path.read_bytes())},
        'original_files': originals, 'final_files': final_files,
        'changed_files': [p.relative_to(ROOT).as_posix() for p in FILES],
        'changes': OPS,
        'source_retrieval': {'workflow_run': 38628335712, 'artifact': 11924802171, 'commit': '254ee805fd6ae7674d3bf2f30e253874255a0eec', 'note': 'Archives temporaires des FI et recommandations. Un téléchargement seul ne vaut pas lecture. Les rubriques pertinentes ont été lues lors de la rédaction des corrections.'},
        'primary_source_sections': {
            'G45-R1': 'Aspirine Cardio, GTIN 7680517950406, Contre-indications',
            'G45-R2': 'Sortis, GTIN 7680540850285, Contre-indications et Effets sur la musculature',
            'G45-R3': 'Eliquis, GTIN 7680615490026, Risque hémorragique et Syndrome des antiphospholipides',
            'E10-R03': 'Baqsimi, GTIN 7680674650010, Interactions',
            'N18-R01': 'Kerendia, GTIN 7680681300014, Traitement associé et CYP3A4',
            'D64-R02/R03': 'Benadon, GTIN 7680256350192, Posologie, Contre-indications et Interactions'},
        'proof_warning': 'Les rapports auteur, registres et passes 1 antérieurs portent sur les anciennes empreintes. Ils restent historiques, non valides comme attestations de cette version. Ce reçu est un delta ciblé, pas un registre exhaustif ni une levée indépendante des 25 réserves.'
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(OPS)} corrections appliquées dans {len(FILES)} fichiers; audits et injection non attestés.')

if __name__ == '__main__':
    main()
