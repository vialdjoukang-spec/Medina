"""Prototype: immutable, per-course Alpha successors of historical publications.

Receipt metadata is evidence of automated work, never human medical approval.
Only the seven existing source files and per-course Alpha figures are eligible.
All legacy guards receive a historical view after actual outputs are verified.
"""
import hashlib
import html
from html.parser import HTMLParser
import json
import re
import subprocess
from datetime import datetime
from urllib.parse import urlsplit

PREFIX = 'organisation/alpha-publications/'
TOUR = 'docs/collaboration/ssp-v2/lancement/2026-10-15/tour1.json'
PLAN = 'docs/collaboration/ssp-v2/2026-10-15/plan-v2.json'
FRAGMENTS = {'S08', 'S05', 'S04', 'S06'}
HISTORICAL_ANCHOR = '8712c3fe758f0c7e1f9fb85378def47b554edb53'
HISTORICAL_RECEIPT = 'organisation/PUBLICATION_EN_ETAT_2026-10-15.json'


class AlphaError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise AlphaError('Publication Alpha : ' + message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def visible_text(raw, course_code=None):
    """Read text, optionally including course content reachable through its tabs.

    Without course context, templates and hidden nodes remain excluded. A known
    course template is cloned by engine/medina_course.js. Only its real .tabs /
    .sci-bar buttons may make their unique local .panel / .sci targets reachable.
    This models available navigation, never initial DOM visibility or a browser
    validation; explicit CSS/ARIA hiding and unrelated templates stay excluded.
    """
    class Node:
        def __init__(self, tag, attrs=(), parent=None):
            self.tag, self.attrs, self.parent = tag, dict(attrs), parent
            self.children = []

        def classes(self):
            return set(self.attrs.get('class', '').split())

        def ancestors(self):
            node = self.parent
            while node is not None:
                yield node
                node = node.parent

    class Text(HTMLParser):
        VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                'link', 'meta', 'param', 'source', 'track', 'wbr'}

        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.document = Node('#document')
            self.stack, self.nodes = [self.document], []

        def handle_starttag(self, tag, attrs):
            node = Node(tag, attrs, self.stack[-1])
            self.stack[-1].children.append(node)
            self.nodes.append(node)
            if tag not in self.VOID:
                self.stack.append(node)

        def handle_startendtag(self, tag, attrs):
            self.handle_starttag(tag, attrs)
            if tag not in self.VOID:
                self.stack.pop()

        def handle_endtag(self, tag):
            for index in range(len(self.stack) - 1, 0, -1):
                if self.stack[index].tag == tag:
                    del self.stack[index:]
                    break

        def handle_data(self, data):
            self.stack[-1].children.append(data)

        @staticmethod
        def explicitly_hidden(node):
            style = re.sub(r'\s+', '', node.attrs.get('style', '')).lower()
            return (node.attrs.get('aria-hidden', '').lower() == 'true' or
                    'display:none' in style or 'visibility:hidden' in style)

        def read(self):
            roots = [node for node in self.nodes if course_code is not None and
                     node.tag == 'template' and node.attrs.get('id') == 'ch-' + course_code]
            # Plain historical fixtures remain supported. Once course templates exist,
            # evidence must come from exactly one known, non-nested course root.
            if course_code is not None and any(n.tag == 'template' and
                                               n.attrs.get('id', '').startswith('ch-') for n in self.nodes):
                if len(roots) != 1 or any(n.tag == 'template' for n in roots[0].ancestors()):
                    return ''
            course = roots[0] if len(roots) == 1 else None
            local = [node for node in self.nodes if course is not None and
                     course in node.ancestors()]
            ids = {}
            for node in local:
                ids.setdefault(node.attrs.get('id'), []).append(node)
            active = {course} if course is not None else set()

            def walk(node, reached, parts):
                if (self.explicitly_hidden(node) or node.tag in {'script', 'style'} or
                        (node.tag == 'template' and node is not course) or
                        ('hidden' in node.attrs and node not in active)):
                    return
                reached.add(node)
                for child in node.children:
                    if isinstance(child, str):
                        if course is None or node is course or course in node.ancestors():
                            parts.append(child)
                    else:
                        walk(child, reached, parts)

            while True:
                reached, parts = set(), []
                walk(self.document, reached, parts)
                additions = set()
                for button in reached:
                    ancestors = list(button.ancestors())
                    if (course is None or course not in ancestors or button.tag != 'button' or
                            'disabled' in button.attrs or button.attrs.get('aria-disabled') == 'true' or
                            any('inert' in n.attrs or (n.tag == 'fieldset' and 'disabled' in n.attrs)
                                for n in [button] + ancestors)):
                        continue
                    for key, target_class, bar_class in (('data-p', 'panel', 'tabs'),
                                                         ('data-s', 'sci', 'sci-bar')):
                        target_id = button.attrs.get(key, '')
                        matches = ids.get(target_id, [])
                        if (not target_id or len(matches) != 1 or
                                ('aria-controls' in button.attrs and
                                 button.attrs['aria-controls'] != target_id) or
                                not any(bar_class in n.classes() for n in ancestors)):
                            continue
                        target = matches[0]
                        if target_class not in target.classes():
                            continue
                        if key == 'data-p':
                            if target_id not in {'pA', 'pE', 'pS', 'pP'}:
                                continue
                        else:
                            # Scientific tabs operate inside this course's science panel.
                            panels = [n for n in ancestors if 'panel' in n.classes()]
                            if (not panels or panels[0].attrs.get('id') != 'pS' or
                                    panels[0] not in target.ancestors()):
                                continue
                        additions.add(target)
                if additions <= active:
                    return ''.join(parts)
                active.update(additions)

    if course_code is not None:
        require(isinstance(course_code, str) and re.fullmatch(r'[A-Z][0-9]{2}', course_code),
                'code de cours requis pour analyser la navigation')
    parser = Text()
    parser.feed(raw.decode('utf-8'))
    return parser.read()


def reachable_course_text(raw, code):
    """Course text reachable after opening its real runtime navigation controls."""
    return visible_text(raw, course_code=code)


def load(tree, path):
    try:
        value = json.loads(tree.read(path))
        require(isinstance(value, dict), 'objet JSON requis : ' + path)
        return value
    except (ValueError, TypeError) as error:
        raise AlphaError('Publication Alpha : JSON invalide : ' + path) from error


def ancestor(root, older, newer):
    require(isinstance(older, str) and re.fullmatch('[0-9a-f]{40}', older), 'SHA immuable requis')
    result = subprocess.run(['git', 'merge-base', '--is-ancestor', older, newer],
                            cwd=root, capture_output=True)
    require(result.returncode == 0, 'commit absent ou hors ascendance : ' + older)


def core_paths(code):
    return {f'chapters/{code}/{code}_{part}.html' for part in ('a', 'b', 'c', 'd', 'pop1', 'pop2')} | {f'glossary/{code.lower()}.py'}


def owned(path, paths):
    return any(path == item or path.startswith(item + '/') for item in paths)


def https_url(value):
    try:
        parsed = urlsplit(value)
        return (isinstance(value, str) and not any(c.isspace() for c in value) and
                parsed.scheme == 'https' and bool(parsed.hostname) and
                parsed.username is None and parsed.password is None)
    except (TypeError, ValueError, AttributeError):
        return False


def figure_rights(source, figure, asset, actor, code, mission_paths):
    """Retain downloaded original bytes and the actual source/licence evidence.

    figure.rights_evidence is {path, sha256}; its committed JSON contains the
    three URLs, original_sha256, author, credit, retrieved_at (ISO timezone),
    license_quote, transformed:false, ai_generated:false, and source_page /
    license_page {path, sha256} references to retained source-page bytes.
    A technical check binds evidence; it does not certify a medical judgement.
    """
    urls = ('original_url', 'source_url', 'license_url')
    require(all(https_url(figure.get(key)) for key in urls), 'URL de figure HTTPS sans identifiants requise')
    require(figure.get('original_sha256') == digest(asset), 'image différente des octets originaux')
    proof = figure.get('rights_evidence', {})
    require(isinstance(proof, dict) and isinstance(proof.get('path'), str) and
            owned(proof['path'], mission_paths), 'preuve de droits hors mission')
    raw = source.read(proof['path'])
    require(proof.get('sha256') == digest(raw), 'empreinte de preuve de droits différente')
    rights = load(source, proof['path'])
    require(rights.get('schema_version') == 1 and rights.get('actor') == actor and rights.get('code') == code and
            rights.get('original_sha256') == digest(asset) and rights.get('transformed') is False and
            rights.get('ai_generated') is False and rights.get('license_verified') is True and
            all(rights.get(key) == figure[key] for key in urls), 'droits ou octets originaux non établis')
    require(all(isinstance(rights.get(key), str) and rights[key].strip() for key in
                ('author', 'credit', 'retrieved_at', 'license_quote')), 'auteur, crédit, date ou citation de licence absents')
    try:
        retrieved = datetime.fromisoformat(rights['retrieved_at'].replace('Z', '+00:00'))
    except ValueError as error:
        raise AlphaError('Publication Alpha : date de consultation invalide') from error
    require(retrieved.tzinfo is not None, 'fuseau de consultation requis')
    require(retrieved <= datetime.now(retrieved.tzinfo), 'date de consultation future')
    pages = {}
    for key in ('source_page', 'license_page'):
        ref = rights.get(key, {})
        require(isinstance(ref, dict) and isinstance(ref.get('path'), str) and
                owned(ref['path'], mission_paths), 'page de droits hors mission')
        page = source.read(ref['path'])
        require(ref.get('sha256') == digest(page), 'page de droits différente de son empreinte')
        pages[key] = page.decode('utf-8', errors='replace')
    require(rights['author'] in pages['source_page'] and rights['credit'] in pages['source_page'] and
            rights['license_quote'] in pages['license_page'], 'auteur, crédit ou licence absent des pages conservées')
    require(rights['credit'] in figure['attribution'], 'attribution différente du crédit vérifié')


class HistoricalView:
    def __init__(self, tree, originals):
        self.root, self.revision = tree.root, tree.revision
        self.actual, self.originals = tree, originals
        self.entries = dict(tree.entries)
        for path, (base, raw) in originals.items():
            if raw is None:
                self.entries.pop(path, None)
            else:
                entry = base.entries[path]
                blob = b'blob ' + str(len(raw)).encode() + b'\0' + raw
                self.entries[path] = (entry[0], entry[1], hashlib.sha1(blob).hexdigest())

    def read(self, path, required=True):
        if path in self.originals:
            raw = self.originals[path][1]
            require(raw is not None or not required, 'source historique absente : ' + path)
            return raw
        return self.actual.read(path, required=required)


def verify(tree, trusted_before=None):
    """Verify all receipts and outputs; return historical view + receipt metadata.

    New receipt approvals must preexist the caller's trusted comparison base.
    Later commits recheck every chain, its source commits and its final blobs.
    """
    try:
        from tools.espace import GitTree
        from tools.ai_session_guard import config, manifest
    except ModuleNotFoundError:
        from espace import GitTree
        from ai_session_guard import config, manifest
    paths = sorted(p for p in tree.entries if p.startswith(PREFIX))
    if not paths:
        if trusted_before is not None:
            require(not any(p.startswith(PREFIX) for p in trusted_before.entries), 'suppression de reçu')
        # Historical callers also validate in-memory proposed transactions.
        # Without Alpha receipts they need neither projection nor a revision.
        return tree, {}
    require(isinstance(getattr(tree, 'revision', None), str),
            'arbre Git immuable requis pour vérifier les reçus Alpha')
    ancestor(tree.root, HISTORICAL_ANCHOR, tree.revision)
    anchor = GitTree(tree.root, HISTORICAL_ANCHOR)
    require(tree.read(HISTORICAL_RECEIPT) == anchor.read(HISTORICAL_RECEIPT), 'reçu historique modifié')
    originals, final, chains, metadata = {}, {}, {}, {}
    new_codes = set()
    for path in paths:
        match = re.fullmatch(PREFIX + r'(Claude|Codex)/([A-Z][0-9]{2})/([0-9]{4})\.json', path)
        require(match is not None, 'chemin de reçu invalide : ' + path)
        actor, code, sequence = match.groups()
        receipt = load(tree, path)
        phase = receipt.get('phase')
        require(phase in {'figures_only', 'provisional', 'completed'}, 'phase Alpha invalide')
        require(receipt.get('schema_version') == 1 and receipt.get('actor') == actor and
                receipt.get('code') == code and receipt.get('medical_human_validation') is False,
                'identité ou absence de validation humaine incorrecte')
        prior = chains.get(code)
        require(int(sequence) == (prior['sequence'] + 1 if prior else 1), 'chaîne incomplète : ' + code)
        require(receipt.get('previous_receipt_sha256') == (prior['sha256'] if prior else None),
                'reçu précédent différent : ' + code)
        base_sha, source_sha = receipt.get('base_commit'), receipt.get('source_commit')
        ancestor(tree.root, base_sha, source_sha)
        ancestor(tree.root, source_sha, tree.revision)
        base, source = GitTree(tree.root, base_sha), GitTree(tree.root, source_sha)
        ancestor(tree.root, HISTORICAL_ANCHOR, base_sha)
        if prior:
            require(base.read(prior['path'], required=False) == prior['raw'], 'précédent reçu absent de la base')
        if trusted_before is not None:
            existing = trusted_before.read(path, required=False)
            if existing is None:
                ancestor(tree.root, base_sha, trusted_before.revision)
            else:
                require(existing == tree.read(path), 'reçu historique réécrit : ' + path)
        plan = load(base, PLAN)
        allocation = [r for r in plan.get('audit', []) + plan.get('production', []) if r.get('code') == code]
        require(len(allocation) == 1 and allocation[0].get('owner') == actor, 'cours attribué à une autre IA : ' + code)
        allocation = allocation[0]
        mission = manifest(tree.root, base_sha, receipt.get('mission'), config(tree.root, base_sha))
        require(mission['role'] == 'integrator' and mission['actor'] == actor and
                mission['owner'] == actor and mission['codes'] == [code], 'mission de publication propre requise')
        require(owned(path, mission['paths']), 'reçu hors mission')
        # The existing audit missions cannot silently acquire canonical paths.
        require(mission.get('alpha_publication') is True, 'mission sans autorisation Alpha explicite')
        fragment = receipt.get('fragment')
        require(fragment in FRAGMENTS and any(row.get('code') == code for row in
                load(base, f'nosology/fragments/{fragment}.json').get('lessons', [])), 'fragment invalide')
        require(allocation.get('fragment') == fragment, 'fragment différent de l’attribution')
        initial_hashes = {p: digest(anchor.read(p)) for p in core_paths(code) if anchor.read(p, required=False) is not None}
        is_new = not initial_hashes
        require(is_new or set(initial_hashes) == core_paths(code), 'sept empreintes historiques requises')
        require(not is_new or mission.get('allow_new_course') is True, 'mission sans autorisation nouveau cours')
        snapshot = {'source_files_sha256': {p: digest(base.read(p)) for p in core_paths(code)
                                                    if base.read(p, required=False) is not None}}
        if is_new:
            new_codes.add(code)
            entry = receipt.get('catalog_entry')
            catalog = json.loads(tree.read('chapters.json'))
            require(isinstance(entry, dict) and entry.get('code') == code and entry.get('integrated') is True and
                    entry.get('owner') == fragment and entry.get('publication_mode') == 'alpha' and
                    [r for r in catalog if r.get('code') == code] == [entry], 'entrée nouveau cours absente ou différente')
            require(owned('chapters.json', mission['paths']), 'catalogue hors mission nouveau cours')
        files = receipt.get('files')
        require(isinstance(files, dict) and core_paths(code) <= set(files), 'sept fichiers finaux requis')
        outputs = {}
        for target, ref in files.items():
            require(target in core_paths(code) or target.startswith(f'assets/img/{code.lower()}/alpha/{actor.lower()}/'),
                    'chemin hors cours : ' + target)
            require(owned(target, mission['paths']) and isinstance(ref, dict), 'source hors mission')
            previous = base.read(target, required=False)
            require(ref.get('previous_sha256') == (digest(previous) if previous is not None else None),
                    'ancienne empreinte différente : ' + target)
            if target in final:
                require(previous is not None and digest(previous) == final[target], 'successeur sans version précédente')
            else:
                historical = anchor.read(target, required=False)
                require(previous == historical, 'première version différente de l’ancre historique : ' + target)
                originals[target] = (anchor, historical)
            source_path = ref.get('source_path')
            require(isinstance(source_path, str) and owned(source_path, mission['paths']) and
                    source_path.startswith('docs/collaboration/ssp-v2/execution/' + mission['id'] + '/'),
                    'livraison hors dossier réservé')
            raw = source.read(source_path)
            require(ref.get('sha256') == digest(raw), 'livraison différente du reçu : ' + target)
            if phase == 'figures_only' and target in core_paths(code):
                if target.endswith('.py'):
                    require(raw == previous, 'figure_only modifie le glossaire')
                else:
                    predicted = previous
                    for replacement in ref.get('figure_replacements', []):
                        old, new = replacement.get('old', ''), replacement.get('new', '')
                        require(re.fullmatch(r'<img\b[^>]*>', old, re.I) is not None and
                                re.fullmatch(r'<img\b[^>]*>', new, re.I) is not None and
                                predicted.count(old.encode()) == 1 and
                                not re.search(r'\son[a-z]+\s*=|javascript:|data:', new, re.I) and
                                any(('src="' + asset + '"') in new for asset in files
                                    if asset.startswith(f'assets/img/{code.lower()}/alpha/{actor.lower()}/')),
                                'remplacement limité à une image propre sans code actif')
                        predicted = predicted.replace(old.encode(), new.encode())
                    for insertion in ref.get('figure_insertions', []):
                        marker, asset = insertion.get('before', ''), insertion.get('asset', '')
                        figure = files.get(asset, {}).get('figure', {})
                        require(asset.startswith(f'assets/img/{code.lower()}/alpha/{actor.lower()}/') and
                                isinstance(figure.get('attribution'), str) and marker and
                                predicted.count(marker.encode()) == 1, 'insertion figure sans repère unique')
                        attribution = html.escape(figure['attribution'], quote=True)
                        addition = ('<figure><img src="' + asset + '" alt="' + attribution +
                                    '"><figcaption>' + attribution + '</figcaption></figure>').encode()
                        predicted = predicted.replace(marker.encode(), addition + marker.encode())
                    require(raw == predicted, 'figure_only change du texte médical')
            outputs[target] = digest(raw)
            final[target] = digest(raw)
            if target.startswith('assets/'):
                figure = ref.get('figure', {})
                require(all(isinstance(figure.get(k), str) and figure[k].strip() for k in
                        ('original_url', 'source_url', 'license', 'attribution', 'visual_review_report')) and
                        figure.get('ai_generated') is False, 'preuve de figure incomplète')
                figure_rights(source, figure, raw, actor, code, mission['paths'])
                review = source.read(figure['visual_review_report'])
                visual = load(source, figure['visual_review_report'])
                require(visual.get('actor') == actor and visual.get('code') == code and
                        visual.get('asset_sha256') == digest(raw) and visual.get('status') == 'reviewed' and
                        visual.get('medical_human_validation') is False and visual.get('anatomy_ai_generated') is False and
                        visual.get('license_verified') is True and bool(visual.get('medical_observations')),
                        'revue visuelle médicale incomplète')
                require(owned(figure['visual_review_report'], mission['paths']) and
                        figure.get('visual_review_sha256') == digest(review), 'contrôle visuel absent')
                html_content = b''.join(source.read(files[p]['source_path']) for p in sorted(core_paths(code)) if p.endswith('.html'))
                captions = re.findall(rb'<figcaption\b[^>]*>(.*?)</figcaption>', html_content, re.I | re.S)
                require(any(figure['attribution'] in visible_text(caption) for caption in captions) and
                        figure['attribution'] in reachable_course_text(html_content, code),
                        'attribution invisible dans le cours')
        if phase != 'completed':
            reserves = receipt.get('visible_reservations')
            require(isinstance(reserves, list) and reserves and all(isinstance(r, str) and r.strip() for r in reserves),
                    'réserves provisoires requises')
            # Reserve text must already exist and remain visible in the course.
            html_content = b''.join(source.read(files[p]['source_path']) for p in sorted(core_paths(code)) if p.endswith('.html'))
            require(all(r in reachable_course_text(html_content, code) for r in reserves), 'réserves absentes du cours')
        audit_kinds = () if phase == 'figures_only' else (('MED', 'LANG', 'SEMIO') if phase == 'completed' else ('MED', 'LANG'))
        for kind in audit_kinds:
            proof = receipt.get('audits', {}).get(kind, {})
            report_path = proof.get('path', '')
            require(owned(report_path, mission['paths']), 'rapport hors mission')
            report_raw = source.read(report_path)
            report = load(source, report_path)
            require(proof.get('sha256') == digest(report_raw) and report.get('actor') == actor and
                    report.get('code') == code and report.get('kind') == kind and
                    report.get('status') == ('closed' if phase == 'completed' else 'provisional') and report.get('medical_human_validation') is False and
                    report.get('source_files_sha256') == snapshot['source_files_sha256'] and
                    report.get('reviewed_files_sha256') == outputs and
                    isinstance(report.get('unresolved_blockers'), list) and
                    (phase != 'completed' or report['unresolved_blockers'] == []) and
                    isinstance(report.get('findings'), list) and isinstance(report.get('evidence'), list) and
                    bool(report['evidence']), 'audit non clos ou version différente : ' + kind)
            if kind == 'SEMIO':
                require(report.get('requirement') == 'fundamental_analytical_semiology', 'sémiologie fondamentale analytique non attestée')
            for finding in report['findings']:
                require((phase != 'completed' or finding.get('status') in {'resolved', 'non_blocking'}) and
                        bool(finding.get('evidence')), 'constat non résolu sans preuve')
            if phase == 'provisional':
                require(all(isinstance(item, str) and item in reachable_course_text(html_content, code)
                            for item in report['unresolved_blockers']), 'blocage provisoire absent du cours')
        chains[code] = dict(sequence=int(sequence), sha256=digest(tree.read(path)), path=path, raw=tree.read(path))
        metadata[code] = dict(receipt=path, receipt_sha256=digest(tree.read(path)), actor=actor,
                              source_commit=source_sha, phase=phase, files=outputs)
    if trusted_before is not None:
        require({p for p in trusted_before.entries if p.startswith(PREFIX)} <= set(paths), 'suppression de reçu')
    for path, expected in final.items():
        require(digest(tree.read(path)) == expected, 'source finale différente du reçu : ' + path)
    if new_codes:
        catalog_rows = [r for r in json.loads(tree.read('chapters.json')) if r.get('code') not in new_codes]
        original_catalog = json.dumps(catalog_rows, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
        originals['chapters.json'] = (tree, original_catalog)
    return HistoricalView(tree, originals), metadata


def views(before, after):
    """For garde: preserve all historical controls on all non-Alpha changes."""
    historical_before, _ = verify(before)
    historical_after, metadata = verify(after, trusted_before=before)
    if ('chapters.json' in getattr(historical_before, 'originals', {}) or
            'chapters.json' in getattr(historical_after, 'originals', {})):
        def normalized(view):
            raw = json.dumps(json.loads(view.read('chapters.json')), ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
            return HistoricalView(view, {'chapters.json': (view, raw)})
        historical_before, historical_after = normalized(historical_before), normalized(historical_after)
    added = {p for p in after.entries if p.startswith(PREFIX)} - set(before.entries)
    if added:
        try:
            from tools.publication_en_etat import HISTORY
        except ModuleNotFoundError:
            from publication_en_etat import HISTORY
        for path in HISTORY:
            require(before.read(path, required=False) == after.read(path, required=False),
                    'publication Alpha modifie un catalogue ou registre historique : ' + path)
        new_catalog_codes = {code for code, item in metadata.items() if item['receipt'] in added and
                             load(after, item['receipt']).get('catalog_entry') is not None}
        before_catalog, after_catalog = json.loads(before.read('chapters.json')), json.loads(after.read('chapters.json'))
        require([r for r in before_catalog if r.get('code') not in new_catalog_codes] ==
                [r for r in after_catalog if r.get('code') not in new_catalog_codes], 'catalogue extérieur modifié')
        for code in new_catalog_codes:
            old_rows = [r for r in before_catalog if r.get('code') == code]
            require(not old_rows or old_rows == [r for r in after_catalog if r.get('code') == code], 'entrée Alpha existante modifiée')
        targets = {p for item in metadata.values() if item['receipt'] in added for p in item['files']}
        changed_assets = {p for p in before.entries.keys() | after.entries.keys()
                          if p.startswith('assets/img/') and before.entries.get(p) != after.entries.get(p)}
        require(changed_assets <= targets, 'asset modifié hors reçu Alpha')
    return historical_before, historical_after, metadata


if __name__ == '__main__':
    import argparse
    from pathlib import Path
    try:
        from tools.espace import GitTree
    except ModuleNotFoundError:
        from espace import GitTree
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--before', required=True)
    parser.add_argument('--after', default='HEAD')
    args = parser.parse_args()
    _, _, verified = views(GitTree(args.root, args.before), GitTree(args.root, args.after))
    print(json.dumps({'alpha_publications': verified, 'medical_human_validation': False}, ensure_ascii=False))
