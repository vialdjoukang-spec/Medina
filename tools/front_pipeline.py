#!/usr/bin/env python3
"""front_pipeline — construire ce qui a changé, contrôler, résumer en cinq lignes.

Orchestrateur déterministe du frontend MEDINA, sans IA, en quatre niveaux :

  N0  git diff depuis une base → cartographie fichiers → cibles (atlas, fragments, pages).
  N1  construction incrémentale : chaque cible a une empreinte de ses entrées réelles,
      relevées par traçage (audit hook) lors de sa dernière construction ; si l'empreinte
      est inchangée, la cible est sautée ou restaurée depuis le cache d'objets.
  N2  contrôles ciblés : tests Python liés, front_poids (poids et budget), verify_*.cjs
      filtrés sur les fragments touchés, front_garde sur un fragment et une leçon touchés.
  N3  rapport JSON, résumé de cinq lignes et, seulement en cas d'échec, un paquet minimal
      (échecs, fichiers suspects, niveau de modèle conseillé) prêt à donner à un agent.

Commande commune (agents et humains) :
    python3 tools/front_pipeline.py                  # base origin/main, arbre de travail
    python3 tools/front_pipeline.py --dry-run        # plan seul, rien n'est exécuté
    python3 tools/front_pipeline.py --fichiers engine/atlas_v4.css   # sans git

Code retour : 0 tout passe ; 1 une construction ou un contrôle échoue ; 2 exécution impossible.
L'outil ne lit ni ne modifie aucun contenu médical : il lance les constructeurs existants.
Documentation : docs/frontend/outils/MOTORISATION.md.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as _dt
import fnmatch
import hashlib
import importlib.util
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
VERSION = 1
CACHE_DEFAUT = Path(os.environ.get('MEDINA_PIPELINE_CACHE') or Path.home() / '.cache' / 'medina-front-pipeline')

# Cibles agrégées : « *fragments » s'étend aux 23 fragments du registre.
FRAGS = '*fragments'
TOUT = ('atlas', FRAGS, 'index', 'organisation', 'apercu')
COEUR_CONSTRUCTION = (
    'build_front.py', 'build_medina.py', 'fragment_surface.py', 'nosologyEngine.py',
    'fragments.json', 'organisation/fragments.json', 'organisation/course_groups.json',
    'tools/glossary_loader.py', 'tools/insert_justifications.py', 'tools/atomic_output.py',
)
# Règles statiques de N0, dans l'ordre : la première qui correspond l'emporte.
# Une cible préfixée par « @ » ne construit rien : elle déclenche seulement des contrôles.
REGLES: list[tuple[str, tuple[str, ...], str]] = [
    *[(chemin, TOUT, 'cœur de construction') for chemin in COEUR_CONSTRUCTION],
    ('engine/*', TOUT, 'moteur commun (engine/*)'),
    ('shell/fragment.*', (FRAGS, 'index'), 'coque des fragments'),
    ('shell/*', TOUT, 'coque commune (shell/*)'),
    ('modules/*', ('atlas', 'fragment:S01'), 'module de l’atlas et de S01'),
    ('glossary/*', ('atlas', FRAGS, 'index'), 'glossaire chargé globalement'),
    ('nosology/*', (FRAGS, 'index'), 'nosologie commune'),
    ('assets/images/*', ('@assemblage',), 'images copiées à l’assemblage'),
    ('assets/img/*', ('@assemblage',), 'images copiées à l’assemblage'),
    ('assets/*', ('atlas', FRAGS, 'index'), 'ressources communes (polices)'),
    ('build_index.py', ('index',), 'portail'),
    ('tools/build_organisation.py', ('organisation',), 'tableau d’organisation'),
    ('organisation/dashboard_template.html', ('organisation',), 'tableau d’organisation'),
    ('organisation/execution-*', (), 'reçus d’exécution'),
    ('organisation/*', ('organisation',), 'données d’organisation'),
    ('tools/build_fragment_work_preview.py', ('apercu',), 'aperçu Infectiologie'),
    ('livraisons/Livraison Codex/I-03-Infectiologie/*', ('apercu',), 'sources de l’aperçu'),
    ('livraisons/*', (), 'livraisons hors construction'),
    ('tools/front_garde.py', ('@garde',), 'outil de contrôle modifié'),
    ('tools/front_poids.py', ('@poids',), 'outil de contrôle modifié'),
    ('tools/front_pipeline.py', ('@pipeline',), 'orchestrateur modifié'),
    ('tests/*', ('@test',), 'test modifié'),
    ('docs/*', (), 'documentation'),
    ('audits/*', (), 'rapports d’audit'),
    ('.github/*', (), 'configuration CI (lue par GitHub, pas par la construction)'),
    ('.claude/*', (), 'configuration des agents'),
    ('*.md', (), 'documentation'),
    ('*.pdf', (), 'document'),
]
SUFFIXES_CODE = {'.py', '.js', '.cjs', '.css', '.html', '.json', '.woff2'}
TAB_RE = re.compile(r'^chapters/([A-Z][0-9]{2}[A-Z0-9.]*)/\1_([abcd])\.html$')
CHAPITRE_RE = re.compile(r'^chapters/([^/]+)/')
# Fichiers dont dépend la logique des filtres de jauge : verify_fragment_filters (tous fragments).
FILTRES_SENSIBLES = ('engine/category_organisation.*', 'nosology/frequency.json', 'nosologyEngine.py',
                     'fragment_surface.py', 'tests/verify_fragment_filters.cjs')

# Budget de non-régression des poids (docs/frontend/outils/POIDS.md, mesure + 10 %).
BUDGET_DEFAUT = {'max': {
    'site.total.brut': 335000000,
    'pages.[MEDINA.html].total.brut': 74300000,
    'pages.[fragments/MEDINA_S08_nerveux.html].total.gzip': 3800000,
    'pages.[index.html].total.gzip': 600000,
}}

# Niveau d'IA conseillé par type d'échec : « leger » = modèle économique (tri, correction
# mécanique d'une valeur, d'un chemin ou d'une durée) ; « opus » = jugement (design,
# régression de comportement, diagnostic). Un échec léger non résolu en deux essais passe à Opus.
NIVEAU_IA = {
    'construction': 'leger', 'tests-python': 'leger', 'front_poids': 'leger',
    'garde:transitions': 'leger', 'garde:mouvement-reduit': 'leger', 'garde:erreurs': 'leger',
    'garde:police': 'leger', 'garde:debordement': 'opus', 'garde:contraste': 'opus',
    'garde:saturation': 'opus', 'garde:cartes': 'opus', 'garde:focus': 'opus', 'garde:axe': 'opus',
    'verify': 'opus',
}
MODELES = {'leger': 'claude-sonnet-5-5 (ou Haiku pour le tri)', 'opus': 'claude-opus-5-5'}


# ===================================================================== N0 : cartographie

@dataclass
class Contexte:
    """Ce que la cartographie doit savoir du dépôt ; injectable pour les tests."""
    fragments: list[str]
    slugs: dict[str, str]
    proprietaire: dict[str, str]                       # code CIM (ou alias couvert) → fragment
    contenu_base: Callable[[str], bytes | None] = lambda chemin: None
    contenu_tete: Callable[[str], bytes | None] = lambda chemin: None
    index_deps: dict[str, list[str]] = field(default_factory=dict)  # dépendance tracée → cibles


@dataclass
class Plan:
    cibles: dict[str, list[str]] = field(default_factory=dict)       # cible → raisons
    declencheurs: dict[str, list[str]] = field(default_factory=dict)  # fichier → cibles
    ignores: list[str] = field(default_factory=list)
    conservateurs: list[str] = field(default_factory=list)            # fichiers non classés
    lecons: dict[str, list[str]] = field(default_factory=dict)        # fragment → codes touchés
    drapeaux: set[str] = field(default_factory=set)                   # @garde, @poids, @test…

    def ajouter(self, chemin: str, cibles, raison: str, ctx: Contexte):
        etendues = []
        for cible in cibles:
            if cible.startswith('@'):
                self.drapeaux.add(cible)
                continue
            for c in (['fragment:' + f for f in ctx.fragments] if cible == FRAGS else [cible]):
                if c.startswith('fragment:') and c[9:] not in ctx.fragments:
                    continue
                etendues.append(c)
                raisons = self.cibles.setdefault(c, [])
                texte = f'{chemin} : {raison}'
                if texte not in raisons:
                    raisons.append(texte)
        self.declencheurs.setdefault(chemin, [])
        for c in etendues:
            if c not in self.declencheurs[chemin]:
                self.declencheurs[chemin].append(c)


def _vide(contenu: bytes | None) -> bool:
    return contenu is None or not contenu.decode('utf-8', 'replace').strip()


def _json(contenu: bytes | None):
    return None if contenu is None else json.loads(contenu.decode('utf-8'))


def _chapitres_json(chemin: str, plan: Plan, ctx: Contexte):
    """Diff champ par champ de chapters.json : seuls les cours modifiés comptent."""
    try:
        avant = {c['code']: c for c in (_json(ctx.contenu_base(chemin)) or [])}
        apres = {c['code']: c for c in (_json(ctx.contenu_tete(chemin)) or [])}
    except (ValueError, KeyError, TypeError):
        plan.ajouter(chemin, TOUT, 'chapters.json illisible : reconstruction complète', ctx)
        return
    codes = sorted(set(avant) | set(apres))
    modifies = [c for c in codes if avant.get(c) != apres.get(c)]
    globaux = [c for c in modifies if c not in avant or c not in apres
               or any(avant[c].get(k) != apres[c].get(k) for k in ('integrated', 'covers', 'owner'))]
    if globaux:
        plan.ajouter(chemin, ('atlas', FRAGS, 'index'),
                     'cours ajouté, retiré, intégré ou couvertures modifiées (' + ', '.join(globaux[:6]) + ') : '
                     'jauge globale et renvois de tous les fragments', ctx)
        return
    for code in modifies:
        fragment = apres[code].get('owner') or ctx.proprietaire.get(code)
        cibles = ('atlas', 'fragment:' + fragment) if fragment else ('atlas', FRAGS, 'index')
        plan.ajouter(chemin, cibles, f'entrée {code} modifiée', ctx)
        if fragment:
            plan.lecons.setdefault(fragment, []).append(code)
    if not modifies:
        plan.ignores.append(chemin)


def _signature_inventaire(contenu: bytes | None):
    donnees = _json(contenu) or {}
    return [{k: v for k, v in lecon.items() if k not in ('plan', 'state')}
            for lecon in donnees.get('lessons', []) if '.' not in lecon.get('code', '')]


def classer(fichiers: list[tuple[str, str]], ctx: Contexte) -> Plan:
    """N0 : (statut git, chemin) → plan des cibles, avec la raison de chaque cible."""
    plan = Plan()
    for statut, chemin in fichiers:
        chemin = chemin.replace('\\', '/')
        chapitre = CHAPITRE_RE.match(chemin)
        if chapitre:
            code = chapitre.group(1)
            fragment = ctx.proprietaire.get(code)
            if not fragment:
                plan.ajouter(chemin, ('atlas', FRAGS, 'index'), f'cours {code} sans fragment propriétaire connu', ctx)
                continue
            plan.ajouter(chemin, ('atlas', 'fragment:' + fragment, 'index'), f'cours {code} du fragment {fragment}', ctx)
            plan.lecons.setdefault(fragment, [])
            if code not in plan.lecons[fragment]:
                plan.lecons[fragment].append(code)
            if TAB_RE.match(chemin) and _vide(ctx.contenu_base(chemin)) != _vide(ctx.contenu_tete(chemin)):
                plan.ajouter(chemin, (FRAGS,), 'onglet vide ↔ rempli : jauge globale de tous les fragments', ctx)
            continue
        if chemin == 'chapters.json':
            _chapitres_json(chemin, plan, ctx)
            continue
        inventaire = re.fullmatch(r'nosology/fragments/([A-Z][0-9]{1,2})\.json', chemin)
        if inventaire:
            ident = inventaire.group(1)
            plan.ajouter(chemin, ('fragment:' + ident, 'index'), f'inventaire nosologique de {ident}', ctx)
            try:
                change = _signature_inventaire(ctx.contenu_base(chemin)) != _signature_inventaire(ctx.contenu_tete(chemin))
            except ValueError:
                change = True
            if change:
                plan.ajouter(chemin, (FRAGS,), 'leçons de l’inventaire modifiées : jauge globale', ctx)
            continue
        for motif, cibles, raison in REGLES:
            if fnmatch.fnmatchcase(chemin, motif):
                if cibles:
                    plan.ajouter(chemin, cibles, raison, ctx)
                else:
                    plan.ignores.append(chemin)
                break
        else:
            connues = ctx.index_deps.get(chemin)
            if connues:
                plan.ajouter(chemin, tuple(connues), 'dépendance relevée par traçage', ctx)
            elif Path(chemin).suffix in SUFFIXES_CODE:
                plan.conservateurs.append(chemin)
                plan.ajouter(chemin, TOUT, 'fichier non classé : reconstruction complète par prudence', ctx)
            else:
                plan.ignores.append(chemin)
    if any(c.startswith('fragment:') for c in plan.cibles) and 'index' not in plan.cibles:
        plan.cibles['index'] = ['portail : agrège les fragments reconstruits']
    return plan


# ===================================================================== git

def git(*args: str, ok_codes=(0,)) -> str:
    r = subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True)
    if r.returncode not in ok_codes:
        raise RuntimeError(f'git {" ".join(args)} : {r.stderr.strip()}')
    return r.stdout


def git_contenu(rev: str, chemin: str) -> bytes | None:
    r = subprocess.run(['git', '-C', str(ROOT), 'show', f'{rev}:{chemin}'], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fichiers_modifies(base: str, tete: str | None) -> list[tuple[str, str]]:
    sortie = git('diff', '--name-status', '--no-renames', base, *([tete] if tete else []))
    fichiers = [tuple(ligne.split('\t', 1)) for ligne in sortie.splitlines() if '\t' in ligne]
    if not tete:
        fichiers += [('A', p) for p in git('ls-files', '--others', '--exclude-standard').splitlines()]
    return sorted(set(fichiers), key=lambda x: x[1])


def contexte_reel(base: str | None, tete: str | None, index_deps=None) -> Contexte:
    fragments = json.loads((ROOT / 'fragments.json').read_text(encoding='utf-8'))
    proprietaire = {}
    try:
        surface = charger_module('fragment_surface', ROOT / 'fragment_surface.py')
        _, owners, courses = surface.frontend_catalog(ROOT)
        proprietaire.update(owners)
        for course in courses.values():
            for code in set(course.get('covers', [])) | {course['code']}:
                proprietaire[code] = course['source_fragment_id']
    except Exception as exc:  # cartographie conservatrice : chaque cours inconnu → tout
        print(f'front_pipeline : propriétaires indisponibles ({exc}) ; cartographie conservatrice', file=sys.stderr)

    def lire_tete(chemin):
        if tete:
            return git_contenu(tete, chemin)
        p = ROOT / chemin
        return p.read_bytes() if p.is_file() else None

    return Contexte(fragments=[f['id'] for f in fragments], slugs={f['id']: f['slug'] for f in fragments},
                    proprietaire=proprietaire,
                    contenu_base=(lambda chemin: git_contenu(base, chemin)) if base else (lambda chemin: None),
                    contenu_tete=lire_tete, index_deps=index_deps or {})


def charger_module(nom: str, chemin: Path):
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    spec = importlib.util.spec_from_file_location('front_pipeline_' + nom, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ===================================================================== N1 : cibles et cache

@dataclass
class Cible:
    id: str
    script: str            # relatif à ROOT
    args: list[str]        # « {out} » remplacé par le dossier de sortie
    sorties: list[str]     # relatives à OUT
    prerequis: list[str] = field(default_factory=list)


def cibles_connues(ctx: Contexte) -> dict[str, Cible]:
    cibles = {'atlas': Cible('atlas', 'build_front.py', [], ['MEDINA.html'])}
    for ident in ctx.fragments:
        cibles['fragment:' + ident] = Cible('fragment:' + ident, 'build_front.py', ['--fragment', ident],
                                            [f'fragments/MEDINA_{ident}_{ctx.slugs[ident]}.html'])
    cibles['index'] = Cible('index', 'build_index.py', ['--fragments-dir', '{out}/fragments', '--output', '{out}/index.html'],
                            ['index.html'], ['fragment:' + i for i in ctx.fragments])
    cibles['organisation'] = Cible('organisation', 'tools/build_organisation.py',
                                   ['--output', '{out}/organisation.html', '--generated-at', '1970-01-01T00:00:00+00:00'],
                                   ['organisation.html'])
    cibles['apercu'] = Cible('apercu', 'tools/build_fragment_work_preview.py', ['--output', '{out}/apercus/infectiologie.html'],
                             ['apercus/infectiologie.html'])
    return cibles


# Exécuté dans le sous-processus de construction : relève fichiers lus et dossiers parcourus.
TRACEUR = r'''
import json, os, runpy, sys
trace, script, *args = sys.argv[1:]
lus, dossiers = set(), set()
ECRITURE = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND
def hook(evenement, a):
    try:
        if evenement == 'open':
            p, mode, drapeaux = a[0], a[1], a[2]
            if p is None or isinstance(p, int):
                return
            if mode is not None:
                if any(x in str(mode) for x in 'wax+'):
                    return
            elif drapeaux & ECRITURE:
                return
            lus.add(os.path.abspath(os.fsdecode(p)))
        elif evenement == 'os.scandir':
            p = a[0]
            if not isinstance(p, int):
                dossiers.add(os.path.abspath(os.fsdecode(p) if p else '.'))
    except Exception:
        pass
sys.addaudithook(hook)
sys.argv = [script, *args]
sys.path.insert(0, os.path.dirname(os.path.abspath(script)))
try:
    runpy.run_path(script, run_name='__main__')
finally:
    with open(trace, 'w', encoding='utf-8') as f:
        json.dump({'lus': sorted(lus), 'dossiers': sorted(dossiers)}, f)
'''


def normaliser(chemin: str, out: Path) -> str | None:
    """Chemin absolu → « r:<relatif à ROOT> » ou « o:<relatif à OUT> » ; None si hors projet."""
    p = Path(chemin)
    if '__pycache__' in p.parts and p.suffix == '.pyc':
        p = p.parent.parent / (p.name.split('.')[0] + '.py')
    for prefixe, base in (('o:', out.resolve()), ('r:', ROOT)):
        try:
            rel = p.resolve().relative_to(base).as_posix()
        except ValueError:
            continue
        if rel.startswith('.git/') or '__pycache__' in rel:
            return None
        return prefixe + rel
    return None


class Cache:
    """État des cibles, mémo des empreintes de fichiers et objets construits."""

    def __init__(self, dossier: Path):
        self.dossier = Path(dossier)
        self.dossier.mkdir(parents=True, exist_ok=True)
        self.verrou = threading.Lock()
        self.etat = self._lire('etat.json', {'version': VERSION, 'cibles': {}})
        if self.etat.get('version') != VERSION:
            self.etat = {'version': VERSION, 'cibles': {}}
        self.memo = self._lire('memo.json', {})

    def _lire(self, nom, defaut):
        try:
            return json.loads((self.dossier / nom).read_text(encoding='utf-8'))
        except (OSError, ValueError):
            return defaut

    def sauver(self):
        with self.verrou:
            for nom, valeur in (('etat.json', self.etat), ('memo.json', self.memo)):
                tmp = self.dossier / (nom + '.tmp')
                tmp.write_text(json.dumps(valeur, ensure_ascii=False, indent=1, sort_keys=True), encoding='utf-8')
                tmp.replace(self.dossier / nom)

    def sha(self, chemin: Path) -> str | None:
        try:
            st = chemin.stat()
        except OSError:
            return None
        if not chemin.is_file():
            return None
        cle = str(chemin)
        signature = [st.st_size, st.st_mtime_ns, st.st_ino]
        with self.verrou:
            connu = self.memo.get(cle)
        if connu and connu[:3] == signature:
            return connu[3]
        h = hashlib.sha256()
        with open(chemin, 'rb') as f:
            for bloc in iter(lambda: f.read(1 << 20), b''):
                h.update(bloc)
        with self.verrou:
            self.memo[cle] = signature + [h.hexdigest()]
        return h.hexdigest()

    def entree(self, cible: str) -> dict | None:
        return self.etat['cibles'].get(cible)

    def enregistrer(self, cible: str, valeur: dict):
        with self.verrou:
            self.etat['cibles'][cible] = valeur

    def objet(self, sha: str) -> Path:
        return self.dossier / 'objets' / sha[:2] / sha

    def stocker(self, chemin: Path, sha: str):
        cible = self.objet(sha)
        if not cible.exists():
            cible.parent.mkdir(parents=True, exist_ok=True)
            tmp = cible.with_suffix('.tmp')
            shutil.copyfile(chemin, tmp)
            tmp.replace(cible)


def resoudre(dep: str, out: Path) -> Path:
    return (out if dep.startswith('o:') else ROOT) / dep[2:]


def deps_effectives(cible: str, deps: list[str], proprietaire: dict[str, str]) -> tuple[list[str], bool]:
    """Retire d'un fragment F les onglets a–d des cours d'autres fragments et leurs inventaires.

    Ces fichiers ne sont lus que pour la jauge globale (onglet vide ou rempli, leçons
    comptées) ; ils sont remplacés par les valeurs dérivées « cours_remplis » et
    « jauge_globale ». Sans cela, toute leçon modifiée invaliderait les 23 fragments.
    """
    if not cible.startswith('fragment:') or not proprietaire:
        return deps, False
    ident = cible[9:]
    gardes = []
    for dep in deps:
        tab = TAB_RE.match(dep[2:]) if dep.startswith('r:') else None
        if tab and proprietaire.get(tab.group(1)) not in (None, ident):
            continue
        inv = re.fullmatch(r'r:nosology/fragments/([A-Z][0-9]{1,2})\.json', dep)
        if inv and inv.group(1) != ident:
            continue
        gardes.append(dep)
    return gardes, len(gardes) != len(deps)


def valeurs_derivees() -> dict | None:
    try:
        moteur = charger_module('nosologyEngine', ROOT / 'nosologyEngine.py')
        cours = moteur.integrated_course_aliases(ROOT)
        return {'cours_remplis': sorted(cours.items()), 'jauge_globale': moteur.global_gauge(ROOT, cours)}
    except Exception:
        return None


def empreinte(cible: Cible, deps: list[str], dossiers: list[str], derives, cache: Cache, out: Path) -> str:
    fichiers = [[d, cache.sha(resoudre(d, out)) or 'absent'] for d in sorted(set(deps))]
    listes = []
    for d in sorted(set(dossiers)):
        p = resoudre(d, out)
        try:
            listes.append([d, sorted(x.name for x in p.iterdir())])
        except OSError:
            listes.append([d, 'absent'])
    contenu = {'v': VERSION, 'py': list(sys.version_info[:2]), 'script': cible.script, 'args': cible.args,
               'fichiers': fichiers, 'dossiers': listes, 'derives': derives}
    return hashlib.sha256(json.dumps(contenu, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def empreinte_entree(cible: Cible, entree: dict, cache: Cache, out: Path, ctx: Contexte, derives) -> str:
    deps, exclu = deps_effectives(cible.id, entree['deps'], ctx.proprietaire)
    dossiers = [d for d in entree.get('dossiers', []) if not (exclu and re.fullmatch(r'r:chapters/[^/]+', d)
                                                                and ctx.proprietaire.get(d[11:]) not in (None, cible.id[9:]))]
    return empreinte(cible, deps, dossiers, derives if exclu else None, cache, out)


REEVALUER = 'prérequis reconstruit : empreinte réévaluée après la phase 1'


@dataclass
class Decision:
    cible: str
    action: str            # construire | restaurer | a_jour | hors_plan
    raison: str
    duree_estimee_s: float = 0.0


def sortie_conforme(cible: Cible, entree: dict, cache: Cache, out: Path) -> bool:
    return all(cache.sha(out / s) == sha for s, sha in entree.get('sorties', {}).items()) and bool(entree.get('sorties'))


def decider(plan: Plan, cibles: dict[str, Cible], cache: Cache, out: Path, ctx: Contexte,
            derives, complet=False, forcees=()) -> dict[str, Decision]:
    """N1 : pour chaque cible, construire, restaurer, garder ou laisser hors plan."""
    decisions: dict[str, Decision] = {}
    requises = set(plan.cibles) | set(forcees) | (set(cibles) if complet else set())
    for cid in list(requises):
        requises |= set(cibles[cid].prerequis) if cid in cibles else set()
    for cid, cible in cibles.items():
        entree = cache.entree(cid)
        duree = (entree or {}).get('duree_s', 0.0)
        if cid in forcees:
            decisions[cid] = Decision(cid, 'construire', 'forcée (--cibles)', duree)
            continue
        if entree:
            if empreinte_entree(cible, entree, cache, out, ctx, derives) == entree['empreinte']:
                if sortie_conforme(cible, entree, cache, out):
                    decisions[cid] = Decision(cid, 'a_jour', 'empreinte des entrées inchangée', duree)
                elif all(cache.objet(sha).exists() for sha in entree['sorties'].values()):
                    decisions[cid] = Decision(cid, 'restaurer', 'entrées inchangées, sortie absente : copie du cache', duree)
                elif cid in requises:
                    decisions[cid] = Decision(cid, 'construire', 'sortie absente et objet hors cache', duree)
                else:
                    decisions[cid] = Decision(cid, 'hors_plan', 'inchangée, sortie absente', duree)
            else:
                raison = '; '.join(plan.cibles.get(cid, [])[:2]) or 'empreinte modifiée hors règles N0 (écart signalé)'
                decisions[cid] = Decision(cid, 'construire', raison, duree)
        elif cid in requises:
            raison = '; '.join(plan.cibles.get(cid, [])[:2]) or 'prérequis d’une cible demandée (cache froid)'
            if not plan.cibles.get(cid) and all((out / s).is_file() for s in cible.sorties) and not complet:
                decisions[cid] = Decision(cid, 'a_jour', 'sortie présente, jamais tracée (non vérifiée)', 0.0)
            else:
                decisions[cid] = Decision(cid, 'construire', raison, 0.0)
        else:
            decisions[cid] = Decision(cid, 'hors_plan', 'non touchée par les fichiers modifiés', duree)
    for cid, cible in cibles.items():
        if (cible.prerequis and decisions[cid].action in ('a_jour', 'restaurer')
                and any(decisions[p].action == 'construire' for p in cible.prerequis if p in decisions)):
            decisions[cid] = Decision(cid, 'construire', REEVALUER, decisions[cid].duree_estimee_s)
    return decisions


def construire(cible: Cible, cache: Cache, out: Path, ctx: Contexte, derives, journaux: Path) -> dict:
    """Construit une cible sous traçage ; enregistre empreinte, dépendances et objets."""
    journaux.mkdir(parents=True, exist_ok=True)
    nom = cible.id.replace(':', '_')
    trace = journaux / f'{nom}.trace.json'
    args = [a.replace('{out}', str(out)) for a in cible.args]
    env = {**os.environ, 'MEDINA_OUT': str(out), 'PYTHONDONTWRITEBYTECODE': '1'}
    debut = time.monotonic()
    with open(journaux / f'{nom}.log', 'w', encoding='utf-8') as journal:
        r = subprocess.run([sys.executable, '-c', TRACEUR, str(trace), str(ROOT / cible.script), *args],
                           cwd=ROOT, env=env, stdout=journal, stderr=subprocess.STDOUT)
    duree = round(time.monotonic() - debut, 1)
    texte = (journaux / f'{nom}.log').read_text(encoding='utf-8', errors='replace')
    if r.returncode != 0:
        return {'statut': 'echec', 'code': r.returncode, 'duree_s': duree, 'extrait': texte.splitlines()[-15:],
                'journal': str(journaux / f'{nom}.log')}
    releve = json.loads(trace.read_text(encoding='utf-8'))
    propres = {'o:' + s for s in cible.sorties}
    deps = sorted({d for d in (normaliser(p, out) for p in releve['lus']) if d and d not in propres
                   and not d.startswith('o:assets/') and not d.startswith('o:images/')
                   and resoudre(d, out).is_file()})  # fichiers temporaires (étape atomique) exclus
    dossiers = sorted({d for d in (normaliser(p, out) for p in releve['dossiers']) if d and not d.startswith('o:')})
    sorties = {}
    for s in cible.sorties:
        sha = cache.sha(out / s)
        if sha is None:
            return {'statut': 'echec', 'code': 0, 'duree_s': duree, 'extrait': [f'sortie attendue absente : {s}'] + texte.splitlines()[-8:]}
        sorties[s] = sha
        if not os.environ.get('MEDINA_PIPELINE_SANS_OBJETS'):
            cache.stocker(out / s, sha)
    entree = {'deps': deps, 'dossiers': dossiers, 'sorties': sorties, 'duree_s': duree,
              'date': _dt.datetime.now().astimezone().isoformat(timespec='seconds')}
    entree['empreinte'] = empreinte_entree(cible, entree, cache, out, ctx, derives)
    cache.enregistrer(cible.id, entree)
    cache.sauver()
    return {'statut': 'ok', 'duree_s': duree, 'deps': len(deps)}


def restaurer(cible: Cible, cache: Cache, out: Path) -> dict:
    entree = cache.entree(cible.id)
    for s, sha in entree['sorties'].items():
        (out / s).parent.mkdir(parents=True, exist_ok=True)
        tmp = out / (s + '.restauration')
        shutil.copyfile(cache.objet(sha), tmp)
        tmp.replace(out / s)
    return {'statut': 'ok', 'duree_s': 0.0, 'restaure': True}


def synchroniser(source: Path, destination: Path) -> int:
    """Copie incrémentale (taille + date) ; renvoie le nombre de fichiers copiés."""
    if not source.is_dir():
        return 0
    copies = 0
    for p in source.rglob('*'):
        if not p.is_file():
            continue
        d = destination / p.relative_to(source)
        st = p.stat()
        if d.is_file() and d.stat().st_size == st.st_size and int(d.stat().st_mtime) == int(st.st_mtime):
            continue
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, d)
        copies += 1
    return copies


def assembler(out: Path) -> int:
    """Même disposition que pages.yml : images à côté de MEDINA.html et des fragments."""
    copies = 0
    for source, cibles in ((ROOT / 'assets/images', ('images', 'fragments/images')),
                           (ROOT / 'assets/img', ('assets/img', 'fragments/assets/img'))):
        for c in cibles:
            copies += synchroniser(source, out / c)
    return copies


# ===================================================================== N2 : contrôles

@dataclass
class Controle:
    id: str
    commande: list[str]
    env: dict[str, str]
    raison: str
    cibles: list[str]
    famille: str            # tests-python | front_poids | verify | garde
    navigateur: bool = False
    rapport: str | None = None


def node_playwright() -> bool:
    if not shutil.which('node'):
        return False
    r = subprocess.run(['node', '-e', "require.resolve('playwright')"], cwd=ROOT / 'tests', capture_output=True)
    return r.returncode == 0


def python_playwright() -> bool:
    return importlib.util.find_spec('playwright') is not None


def tests_python_lies(fichiers: list[str]) -> list[str]:
    tests = set()
    for chemin in fichiers:
        p = Path(chemin)
        if p.suffix != '.py':
            continue
        if p.parts[:1] == ('tests',) and p.name.startswith('test_'):
            tests.add(p.as_posix())
        elif (ROOT / 'tests' / f'test_{p.stem}.py').is_file():
            tests.add(f'tests/test_{p.stem}.py')
    return sorted(tests)


def planifier_controles(plan: Plan, fichiers: list[str], reconstruites: list[str], out: Path, qa: Path,
                        ctx: Contexte, options) -> list[Controle]:
    """N2 : contrôles du moins cher au plus cher, limités aux cibles touchées."""
    controles = []
    tests = tests_python_lies(fichiers)
    if tests:
        modules = [t[:-3].replace('/', '.') for t in tests]
        controles.append(Controle('tests-python', [sys.executable, '-m', 'unittest', *modules], {},
                                  'tests liés aux fichiers Python modifiés', [], 'tests-python'))
    touchees = sorted(set(reconstruites) | set(plan.cibles))
    fragments = [c[9:] for c in touchees if c.startswith('fragment:')]
    produit = [c for c in touchees if c in ('atlas', 'index') or c.startswith('fragment:')]
    if produit or '@poids' in plan.drapeaux:
        budget = qa / 'budget_poids.json'
        commande = [sys.executable, str(ROOT / 'tools/front_poids.py'), '--out', str(out), '--json', str(qa / 'front_poids.json'),
                    '--budget', str(budget)]
        if not options.poids_navigateur:
            commande.append('--sans-navigateur')
        controles.append(Controle('front_poids', commande, {}, 'poids des pages reconstruites et budget', produit,
                                  'front_poids', options.poids_navigateur, str(qa / 'front_poids.json')))
    ids = ','.join(fragments)
    if fragments:
        controles.append(Controle('verify_fragment_bootstrap', ['node', 'tests/verify_fragment_bootstrap.cjs'],
                                  {'MEDINA_OUT': str(out), 'MEDINA_QA_FRAGMENTS': ids, 'MEDINA_QA_OUT': str(qa / 'bootstrap')},
                                  'premier affichage des fragments reconstruits', ['fragment:' + f for f in fragments], 'verify', True))
        controles.append(Controle('verify_category_progress', ['node', 'tests/verify_category_progress.cjs'],
                                  {'MEDINA_OUT': str(out), 'MEDINA_CATEGORY_FRAGMENT_IDS': ids, 'MEDINA_TEST_COMPACT': '1',
                                   'MEDINA_QA_OUT': str(qa / 'categories-progress')},
                                  'jauges de catégorie des fragments reconstruits', ['fragment:' + f for f in fragments], 'verify', True))
    if fragments and getattr(options, 'verify_categories', False):
        controles.append(Controle('verify_categories', ['node', 'tests/verify_categories.cjs'],
                                  {'MEDINA_FRAGMENTS': str(out / 'fragments'), 'MEDINA_CATEGORY_FRAGMENT_IDS': ids,
                                   'MEDINA_QA_OUT': str(qa / 'categories')},
                                  'catégories des fragments reconstruits', ['fragment:' + f for f in fragments], 'verify', True))
    if any(fnmatch.fnmatchcase(f, m) for f in fichiers for m in FILTRES_SENSIBLES):
        controles.append(Controle('verify_fragment_filters', ['node', 'tests/verify_fragment_filters.cjs'],
                                  {'MEDINA_OUT': str(out), 'MEDINA_QA_OUT': str(qa / 'filters')},
                                  'logique des filtres modifiée : tous les fragments', ['fragment:' + f for f in ctx.fragments],
                                  'verify', True))
    # front_garde : fragments avec des leçons touchées d'abord, puis les autres ; S08 par défaut.
    garde = sorted(fragments, key=lambda f: (not plan.lecons.get(f), ctx.fragments.index(f)))[:options.garde_max]
    if not garde and ('index' in touchees or '@garde' in plan.drapeaux):
        garde = ['S08']
    for ident in garde:
        rapport = qa / f'front_garde_{ident}.json'
        commande = [sys.executable, str(ROOT / 'tools/front_garde.py'), '--out', str(out), '--fragment', ident,
                    '--json', str(rapport), *shlex.split(options.garde_args or '')]
        lecon = (plan.lecons.get(ident) or [None])[0]
        if lecon:
            commande += ['--lecon', lecon]
        controles.append(Controle(f'front_garde:{ident}', commande, {}, 'qualité visuelle et accessibilité',
                                  ['fragment:' + ident, 'index'], 'garde', True, str(rapport)))
    return controles


def budget_filtre(budget: dict, out: Path, avec_navigateur: bool) -> dict:
    """Ne garde que les métriques mesurables ici : pages présentes, temps seulement avec navigateur."""
    gardes = {}
    for chemin, limite in budget.get('max', {}).items():
        page = re.match(r'pages\.\[(.+?)\]', chemin)
        if page and not (out / page.group(1)).is_file():
            continue
        if not avec_navigateur and chemin.split('.')[0] in ('temps', 'couverture'):
            continue
        gardes[chemin] = limite
    return {'max': gardes}


def echecs_detail(controle: Controle, code: int, texte: str) -> list[dict]:
    """Liste minimale des échecs : ce qu'un agent doit lire, rien de plus."""
    if controle.famille == 'garde' and controle.rapport and Path(controle.rapport).is_file():
        try:
            rapport = json.loads(Path(controle.rapport).read_text(encoding='utf-8'))
            sortie = []
            for r in rapport.get('resultats', []):
                if r.get('statut') != 'echec':
                    continue
                d = r.get('detail', {})
                exemple = (d.get('echecs') or d.get('sans_indicateur') or d.get('coupables') or d.get('erreurs') or [])[:2]
                sortie.append({'controle': f"garde:{r.get('controle')}", 'page': r.get('page'), 'largeur': r.get('largeur'),
                               'exemples': exemple})
            if sortie:
                return sortie
        except (OSError, ValueError):
            pass
    if controle.famille == 'front_poids' and controle.rapport and Path(controle.rapport).is_file():
        try:
            b = json.loads(Path(controle.rapport).read_text(encoding='utf-8')).get('budget', {})
            sortie = [{'controle': 'front_poids', 'metrique': d['metrique'], 'valeur': d['valeur'], 'limite': d['limite']}
                      for d in b.get('depassements', [])]
            sortie += [{'controle': 'front_poids', 'metrique': m, 'non_mesuree': True} for m in b.get('non_mesurees', [])]
            if sortie:
                return sortie
        except (OSError, ValueError):
            pass
    lignes = [l for l in texte.splitlines() if l.strip()]
    utiles = [l for l in lignes if re.search(r'Error|Erreur|ÉCHEC|FAIL|assert|Traceback|échec', l, re.I)]
    return [{'controle': controle.id, 'code': code, 'extrait': (utiles[-6:] or []) + lignes[-6:]}]


def cle_controle(controle: Controle, cache: Cache, out: Path) -> str | None:
    """Clé d'un contrôle navigateur réussi : commande, outils et octets exacts contrôlés.

    Un contrôle déjà réussi sur les mêmes sorties, avec les mêmes outils, n'est pas relancé
    (CI rejouée, relance après une correction qui ne touche pas cette cible).
    """
    if controle.famille not in ('verify', 'garde'):
        return None
    sorties = {}
    for cid in controle.cibles:
        entree = cache.entree(cid)
        if not entree or not entree.get('sorties'):
            return None
        for chemin, sha in entree['sorties'].items():
            if cache.sha(out / chemin) != sha:
                return None
            sorties[chemin] = sha
    outils = {}
    for x in controle.commande:
        if x.endswith(('.py', '.cjs')):
            p = Path(x) if Path(x).is_absolute() else ROOT / x
            outils[x.replace(str(ROOT), '{root}')] = cache.sha(p)
    outils['tests/browser_runtime.cjs'] = cache.sha(ROOT / 'tests/browser_runtime.cjs')
    contenu = {'v': VERSION, 'commande': [x for x in controle.commande if not x.endswith('.json')],
               'env': {k: v for k, v in controle.env.items() if 'QA_OUT' not in k}, 'outils': outils, 'sorties': sorties}
    return hashlib.sha256(json.dumps(contenu, sort_keys=True).encode()).hexdigest()


def executer_controle(controle: Controle, qa: Path) -> dict:
    qa.mkdir(parents=True, exist_ok=True)
    debut = time.monotonic()
    journal = qa / (controle.id.replace(':', '_') + '.log')
    try:
        with open(journal, 'w', encoding='utf-8') as f:
            r = subprocess.run(controle.commande, cwd=ROOT, env={**os.environ, **controle.env}, stdout=f,
                               stderr=subprocess.STDOUT, timeout=3600)
        code = r.returncode
    except subprocess.TimeoutExpired:
        code = 124
    except FileNotFoundError as exc:
        return {'id': controle.id, 'statut': 'indisponible', 'raison': str(exc), 'duree_s': 0.0}
    texte = journal.read_text(encoding='utf-8', errors='replace')
    duree = round(time.monotonic() - debut, 1)
    if controle.famille == 'garde' and code == 2:
        return {'id': controle.id, 'statut': 'indisponible', 'raison': 'navigateur absent (front_garde code 2)',
                'duree_s': duree, 'journal': str(journal)}
    resultat = {'id': controle.id, 'statut': 'ok' if code == 0 else 'echec', 'code': code, 'duree_s': duree,
                'journal': str(journal), 'octets_journal': len(texte.encode()) + (Path(controle.rapport).stat().st_size if controle.rapport and Path(controle.rapport).is_file() else 0)}
    if code != 0:
        resultat['echecs'] = echecs_detail(controle, code, texte)
    return resultat


# ===================================================================== N3 : rapport et paquet

def niveau_ia(echecs: list[dict]) -> str:
    niveaux = [NIVEAU_IA.get(e.get('controle', ''), NIVEAU_IA.get(e.get('controle', '').split(':')[0].split('_')[0], 'opus'))
               for e in echecs]
    return 'opus' if 'opus' in niveaux or not niveaux else 'leger'


def suspects(cibles_echouees: set[str], plan: Plan, fichiers: list[str]) -> list[str]:
    trouves = [f for f, cibles in plan.declencheurs.items() if set(cibles) & cibles_echouees]
    trouves += [f for f in fichiers if Path(f).suffix in ('.css', '.js', '.py') and f.startswith(('engine/', 'shell/', 'tools/'))
                and f not in trouves and plan.declencheurs.get(f)]
    return trouves[:20]


def resume_cinq_lignes(r: dict) -> list[str]:
    fichiers = r['fichiers']
    c = r['constructions']
    compte = lambda action: [k for k, v in c.items() if v['decision'] == action]
    construites, restaurees, a_jour = compte('construire'), compte('restaurer'), compte('a_jour')
    ctrl = r['controles']
    ok = [x for x in ctrl if x['statut'] == 'ok']
    ko = [x for x in ctrl if x['statut'] == 'echec']
    indispo = [x for x in ctrl if x['statut'] == 'indisponible']
    eco = r['economie']
    lignes = [
        f"front_pipeline · {r['base'] or 'liste explicite'} → {r['tete'] or 'arbre de travail'} · "
        f"{len(fichiers)} fichiers modifiés ({len(r['ignores'])} sans effet, {len(r['conservateurs'])} non classés)",
        f"N0 plan : {len(r['plan'])} cibles touchées sur {len(c)}"
        + (f" ({', '.join(sorted(r['plan'])[:6])}{'…' if len(r['plan']) > 6 else ''})" if r['plan'] else ''),
        f"N1 construction : {len(construites)} à construire, {len(restaurees)} restaurées, {len(a_jour)} à jour"
        + (f" · {eco['construction_realisee_s']:.0f} s réalisés, ≈ {eco['construction_evitee_s']:.0f} s évités" if not r['dry_run'] else ' (plan seul)'),
        (f"N2 contrôles : {len(r['controles_planifies'])} planifiés (plan seul)" if r['dry_run'] else
         f"N2 contrôles : {len(ok)}/{len(ctrl)} ok" + (f", {len(indispo)} indisponibles" if indispo else '')
         + (" · échec : " + ', '.join(x['id'] for x in ko) if ko else '')),
        ("N3 : IA requise — niveau " + r['ia']['niveau'] + f" ({MODELES[r['ia']['niveau']]}) · paquet : {r['ia']['paquet']}"
         if r['ia'] else 'N3 : aucune IA nécessaire'),
    ]
    return lignes


def paquet_agent(r: dict, dossier: Path) -> tuple[str, int]:
    """Texte minimal pour un agent ; renvoie le chemin et une estimation des jetons."""
    echecs = r['echecs']
    lignes = ['Mission MEDINA frontend : corriger les échecs ci-dessous sans toucher au contenu médical '
              '(chapters/, glossary/, nosology/, chapters.json interdits).',
              f"Base {r['base']} ; contrôles relancés par : python3 tools/front_pipeline.py",
              f"Niveau conseillé : {r['ia']['niveau']} ({MODELES[r['ia']['niveau']]}).", '', 'Échecs :']
    for e in echecs:
        lignes.append('- ' + json.dumps(e, ensure_ascii=False)[:600])
    lignes += ['', 'Fichiers suspects (modifiés et liés aux cibles en échec) :']
    lignes += ['- ' + s for s in r['ia']['suspects']] or ['- (aucun : régression préexistante ou environnement)']
    lignes += ['', 'Lire seulement ces fichiers et les journaux cités ; ne pas relancer de construction complète.',
               'Si aucun fichier suspect n’explique l’échec, vérifier d’abord qu’il existe déjà sur la base '
               '(échec préexistant à signaler, non à corriger dans cette mission).']
    texte = '\n'.join(lignes) + '\n'
    chemin = dossier / 'paquet_agent.txt'
    chemin.write_text(texte, encoding='utf-8')
    (dossier / 'paquet_agent.json').write_text(json.dumps({'echecs': echecs, **r['ia']}, ensure_ascii=False, indent=1),
                                               encoding='utf-8')
    return str(chemin), len(texte) // 4


# ===================================================================== principal

def principal(argv=None) -> int:
    ap = argparse.ArgumentParser(description='Construire ce qui a changé, contrôler, résumer en cinq lignes.')
    ap.add_argument('--base', default='origin/main', help='révision de base (défaut origin/main, via merge-base)')
    ap.add_argument('--tete', help='révision de tête pour le diff (défaut : arbre de travail + non suivis)')
    ap.add_argument('--sans-merge-base', action='store_true', help='comparer directement à --base')
    ap.add_argument('--fichiers', nargs='+', help='liste explicite de fichiers modifiés (remplace git diff)')
    ap.add_argument('--cache', type=Path, default=CACHE_DEFAUT, help=f'cache (défaut {CACHE_DEFAUT})')
    ap.add_argument('--out', type=Path, help='dossier de site construit (défaut <cache>/site)')
    ap.add_argument('--dry-run', action='store_true', help='affiche le plan N0–N2 sans rien exécuter')
    ap.add_argument('--jusqua', choices=('plan', 'construction', 'controles'), default='controles')
    ap.add_argument('--jobs', type=int, default=2, help='constructions parallèles (défaut 2 ; ~0,5 Go chacune)')
    ap.add_argument('--complet', action='store_true', help='construire aussi les cibles absentes non touchées')
    ap.add_argument('--cibles', default='', help='cibles forcées, séparées par des virgules (atlas,fragment:S08…)')
    ap.add_argument('--exclure', default='', help='cibles jamais construites ici (ex. atlas pour une boucle de fragment)')
    ap.add_argument('--sans-navigateur', action='store_true', help='omettre les contrôles navigateur')
    ap.add_argument('--sans-cache-controles', action='store_true', help='relancer les contrôles déjà réussis sur les mêmes sorties')
    ap.add_argument('--verify-categories', action='store_true',
                    help='ajoute verify_categories.cjs (hors pages.yml ; en échec sur main 9e1b1d4)')
    ap.add_argument('--garde-max', type=int, default=2, help='fragments contrôlés par front_garde (défaut 2)')
    ap.add_argument('--garde-args', default='', help='arguments ajoutés à front_garde (ex. "--axe /chemin/axe.min.js")')
    ap.add_argument('--budget', type=Path, help='budget JSON de front_poids (défaut : budget de POIDS.md)')
    ap.add_argument('--poids-navigateur', action='store_true', help='front_poids mesure aussi les temps (lent)')
    ap.add_argument('--rapport', type=Path, help='rapport JSON (défaut <cache>/dernier/rapport.json)')
    ap.add_argument('--ia-commande', help='commande lancée seulement en cas d’échec, paquet sur stdin ; {modele} remplacé')
    ap.add_argument('--json', action='store_true', help='imprime le rapport JSON complet')
    a = ap.parse_args(argv)

    cache = Cache(a.cache)
    out = (a.out or a.cache / 'site').resolve()
    dernier = (a.rapport.parent if a.rapport else a.cache / 'dernier').resolve()
    dernier.mkdir(parents=True, exist_ok=True)
    qa = dernier / 'qa'
    try:
        if a.fichiers:
            base, tete, fichiers = None, None, [('M', f) for f in a.fichiers]
        else:
            base = a.base if a.sans_merge_base else git('merge-base', a.base, a.tete or 'HEAD').strip()
            tete = a.tete
            fichiers = fichiers_modifies(base, tete)
    except RuntimeError as exc:
        print(f'front_pipeline : {exc}', file=sys.stderr)
        return 2
    # Index inverse « dépendance tracée → cibles » pour les fichiers que les règles ignorent.
    index_deps: dict[str, list[str]] = {}
    for cid, entree in cache.etat['cibles'].items():
        for d in entree.get('deps', []):
            if d.startswith('r:'):
                index_deps.setdefault(d[2:], []).append(cid)
    ctx = contexte_reel(base, tete, index_deps)
    plan = classer(fichiers, ctx)
    cibles = cibles_connues(ctx)
    forcees = [c for c in a.cibles.split(',') if c]
    inconnues = [c for c in forcees if c not in cibles]
    if inconnues:
        ap.error('cibles inconnues : ' + ', '.join(inconnues))
    derives = valeurs_derivees()
    decisions = decider(plan, cibles, cache, out, ctx, derives, a.complet, forcees)
    for c in [c for c in a.exclure.split(',') if c]:
        if c not in cibles:
            ap.error('cible à exclure inconnue : ' + c)
        if decisions[c].action != 'a_jour':
            decisions[c] = Decision(c, 'hors_plan', 'exclue (--exclure) : sortie éventuellement périmée', decisions[c].duree_estimee_s)
    chemins = [f for _, f in fichiers]
    rapport = {'outil': 'front_pipeline', 'version': VERSION, 'date': _dt.datetime.now().astimezone().isoformat(timespec='seconds'),
               'dry_run': a.dry_run, 'base': base[:12] if base else None, 'tete': tete, 'out': str(out),
               'fichiers': [{'statut': s, 'chemin': f} for s, f in fichiers], 'ignores': plan.ignores,
               'conservateurs': plan.conservateurs, 'plan': plan.cibles, 'drapeaux': sorted(plan.drapeaux),
               'lecons': plan.lecons, 'constructions': {}, 'controles': [], 'echecs': [], 'ia': None}
    a_construire = [d.cible for d in decisions.values() if d.action == 'construire']
    ecarts = [d.cible for d in decisions.values() if d.action == 'construire' and d.cible not in plan.cibles and d.cible not in forcees
              and 'écart' in d.raison]
    rapport['ecarts_cartographie'] = ecarts
    # Les prérequis reconstruits à froid (fragments pour le portail) ne sont pas contrôlés : seules
    # les cibles touchées, forcées ou en écart de cartographie le sont.
    controlables = set(plan.cibles) | set(forcees) | set(ecarts)
    for d in decisions.values():
        rapport['constructions'][d.cible] = {'decision': d.action, 'raison': d.raison, 'duree_estimee_s': d.duree_estimee_s}

    if a.dry_run or a.jusqua == 'plan':
        controles = planifier_controles(plan, chemins, [c for c in a_construire if c in controlables], out, qa, ctx, a)
        rapport['controles_planifies'] = [{'id': c.id, 'raison': c.raison, 'navigateur': c.navigateur,
                                           'commande': ' '.join(shlex.quote(x) for x in c.commande),
                                           'env': c.env} for c in controles]
        rapport['economie'] = economie(decisions, {})
        return terminer(rapport, a, dernier, plan, chemins, afficher_plan=True)

    # ----- N1 : construction
    out.mkdir(parents=True, exist_ok=True)
    journaux = dernier / 'constructions'
    resultats: dict[str, dict] = {}
    echouees: set[str] = set()
    for d in decisions.values():
        if d.action == 'restaurer':
            resultats[d.cible] = restaurer(cibles[d.cible], cache, out)
    # Les plus longues d'abord (durées connues ; l'atlas en tête à froid) : meilleure répartition.
    phase1 = sorted((c for c in a_construire if not cibles[c].prerequis),
                    key=lambda c: (-decisions[c].duree_estimee_s, c != 'atlas'))
    phase2 = [c for c in a_construire if cibles[c].prerequis]
    with cf.ThreadPoolExecutor(max_workers=max(1, a.jobs)) as pool:
        futurs = {pool.submit(construire, cibles[c], cache, out, ctx, derives, journaux): c for c in phase1}
        for futur in cf.as_completed(futurs):
            c = futurs[futur]
            resultats[c] = futur.result()
            print(f"  {c} : {resultats[c]['statut']} ({resultats[c]['duree_s']} s)", file=sys.stderr, flush=True)
    for c in phase2:
        manquants = [p for p in cibles[c].prerequis if not all((out / s).is_file() for s in cibles[p].sorties)]
        if manquants:
            resultats[c] = {'statut': 'bloque', 'duree_s': 0.0, 'extrait': ['prérequis absents : ' + ', '.join(manquants[:6])]}
            continue
        entree = cache.entree(c)
        if (decisions[c].raison == REEVALUER and entree and sortie_conforme(cibles[c], entree, cache, out)
                and empreinte_entree(cibles[c], entree, cache, out, ctx, derives) == entree['empreinte']):
            resultats[c] = {'statut': 'ok', 'duree_s': 0.0, 'restaure': True, 'note': 'prérequis identiques : inchangée'}
            continue
        resultats[c] = construire(cibles[c], cache, out, ctx, derives, journaux)
        print(f"  {c} : {resultats[c]['statut']} ({resultats[c]['duree_s']} s)", file=sys.stderr, flush=True)
    for c, res in resultats.items():
        rapport['constructions'][c].update(res)
        if res['statut'] in ('echec', 'bloque'):
            echouees.add(c)
            rapport['echecs'].append({'controle': 'construction', 'cible': c, 'extrait': res.get('extrait', [])})
    rapport['assemblage_fichiers_copies'] = assembler(out)
    rapport['economie'] = economie(decisions, resultats)
    cache.sauver()

    # ----- N2 : contrôles
    if a.jusqua == 'controles':
        reconstruites = [c for c in a_construire if c in controlables and resultats.get(c, {}).get('statut') == 'ok']
        controles = planifier_controles(plan, chemins, reconstruites, out, qa, ctx, a)
        qa.mkdir(parents=True, exist_ok=True)
        budget = json.loads(a.budget.read_text(encoding='utf-8')) if a.budget else BUDGET_DEFAUT
        (qa / 'budget_poids.json').write_text(json.dumps(budget_filtre(budget, out, a.poids_navigateur)), encoding='utf-8')
        avec_node = node_playwright()
        avec_py = python_playwright()
        for controle in controles:
            if set(controle.cibles) & echouees:
                rapport['controles'].append({'id': controle.id, 'statut': 'indisponible', 'raison': 'construction en échec', 'duree_s': 0})
                continue
            if controle.navigateur and (a.sans_navigateur or (controle.famille == 'verify' and not avec_node)
                                        or (controle.famille == 'garde' and not avec_py)):
                rapport['controles'].append({'id': controle.id, 'statut': 'indisponible', 'duree_s': 0,
                                             'raison': '--sans-navigateur' if a.sans_navigateur else 'Playwright absent'})
                continue
            cle = cle_controle(controle, cache, out) if not a.sans_cache_controles else None
            deja = cache.etat.setdefault('controles', {}).get(cle) if cle else None
            if deja:
                rapport['controles'].append({'id': controle.id, 'statut': 'ok', 'duree_s': 0.0, 'cache': True,
                                             'raison': f"déjà réussi le {deja['date']} sur ces mêmes sorties",
                                             'duree_evitee_s': deja['duree_s'], 'cibles': controle.cibles})
                print(f"  {controle.id} : ok (cache, {deja['duree_s']} s évités)", file=sys.stderr, flush=True)
                continue
            res = executer_controle(controle, qa)
            if cle and res['statut'] == 'ok':
                with cache.verrou:
                    cache.etat['controles'][cle] = {'id': controle.id, 'duree_s': res['duree_s'],
                                                    'date': _dt.datetime.now().astimezone().isoformat(timespec='seconds')}
                cache.sauver()
            res['cibles'] = controle.cibles
            res['famille'] = controle.famille
            rapport['controles'].append(res)
            print(f"  {controle.id} : {res['statut']} ({res['duree_s']} s)", file=sys.stderr, flush=True)
            for e in res.get('echecs', []):
                rapport['echecs'].append({**e, 'cibles': controle.cibles})
    return terminer(rapport, a, dernier, plan, chemins)


def economie(decisions: dict[str, Decision], resultats: dict[str, dict]) -> dict:
    realise = sum(r.get('duree_s', 0.0) for r in resultats.values() if not r.get('restaure'))
    connu = {c: d.duree_estimee_s for c, d in decisions.items()}
    complet = sum(connu.values())
    evite = sum(d.duree_estimee_s for d in decisions.values() if d.action in ('a_jour', 'restaurer', 'hors_plan'))
    return {'construction_realisee_s': round(realise, 1), 'construction_evitee_s': round(evite, 1),
            'construction_complete_estimee_s': round(complet, 1),
            'cibles_sans_duree_connue': sorted(c for c, v in connu.items() if not v)}


def terminer(rapport: dict, a, dernier: Path, plan: Plan, chemins: list[str], afficher_plan=False) -> int:
    for ancien in ('paquet_agent.txt', 'paquet_agent.json'):  # jamais de paquet périmé après un succès
        (dernier / ancien).unlink(missing_ok=True)
    if rapport['echecs']:
        cibles_ko = {c for e in rapport['echecs'] for c in (e.get('cibles') or [e.get('cible')]) if c}
        rapport['ia'] = {'niveau': niveau_ia(rapport['echecs']), 'suspects': suspects(cibles_ko, plan, chemins)}
        rapport['ia']['modele'] = MODELES[rapport['ia']['niveau']]
        rapport['ia']['paquet'], rapport['ia']['jetons_estimes_paquet'] = paquet_agent(rapport, dernier)
        journaux = sum(c.get('octets_journal', 0) for c in rapport['controles'])
        rapport['ia']['jetons_estimes_journaux_bruts'] = journaux // 4
    rapport['resume'] = resume_cinq_lignes(rapport)
    cible = a.rapport or dernier / 'rapport.json'
    Path(cible).write_text(json.dumps(rapport, ensure_ascii=False, indent=1), encoding='utf-8')
    if afficher_plan:
        print('Plan N0 (cible ← raisons) :')
        for c, raisons in sorted(rapport['plan'].items()):
            print(f'  {c} ← {raisons[0]}' + (f' (+{len(raisons) - 1})' if len(raisons) > 1 else ''))
        print('Décisions N1 :')
        for c, d in rapport['constructions'].items():
            if d['decision'] != 'hors_plan':
                print(f"  {c} : {d['decision']} — {d['raison']}")
        print('Contrôles N2 :')
        for c in rapport.get('controles_planifies', []):
            print(f"  {c['id']} : {c['raison']}" + (' [navigateur]' if c['navigateur'] else ''))
    if a.json:
        print(json.dumps(rapport, ensure_ascii=False, indent=1))
    print('\n'.join(rapport['resume']))
    print(f'Rapport : {cible}')
    if rapport['ia'] and a.ia_commande and not rapport['dry_run']:
        commande = a.ia_commande.replace('{modele}', rapport['ia']['niveau'])
        with open(rapport['ia']['paquet'], encoding='utf-8') as paquet:
            subprocess.run(commande, shell=True, stdin=paquet, cwd=ROOT)
    return 1 if rapport['echecs'] else 0


if __name__ == '__main__':
    sys.exit(principal())
