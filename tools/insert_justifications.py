#!/usr/bin/env python3
"""Compile contextual medical explanations without rewriting canonical lessons.

Targets are explicit: source file, existing ancestor id, literal visible text,
and optional occurrence. Ambiguous, interactive or overlapping targets fail.
Compilation is a technical check, never a medical certification.
"""
import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import urlsplit


class JustificationError(ValueError):
    pass


VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
BLOCKED = {'a', 'button', 'script', 'style', 'svg', 'textarea', 'select', 'option'}


class TextParser(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.source = source
        self.lines = [0] + [m.end() for m in re.finditer('\n', source)]
        self.stack = []
        self.nodes = []
        self.feed(source)

    def source_offset(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        blocked = tag in BLOCKED or 'data-k' in attrs or 'data-ab' in attrs or attrs.get('role') in {'button', 'link'} or 'contenteditable' in attrs
        blocked |= tag == 'template' and not attrs.get('id', '').startswith('ch-')
        if tag not in VOID:
            self.stack.append((tag, attrs.get('id'), blocked))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def add(self, raw):
        if not raw or any(item[2] for item in self.stack):
            return
        start = self.source_offset()
        ancestors = tuple(item[1] for item in self.stack if item[1])
        if self.nodes and self.nodes[-1]['end'] == start and self.nodes[-1]['ancestors'] == ancestors:
            self.nodes[-1]['end'] = start + len(raw)
        else:
            self.nodes.append({'start': start, 'end': start + len(raw), 'ancestors': ancestors})

    def handle_data(self, data):
        self.add(data)

    def handle_entityref(self, name):
        self.add('&' + name + ';')

    def handle_charref(self, name):
        self.add('&#' + name + ';')


def _text_nodes(source):
    return TextParser(source).nodes


def _decoded_positions(raw):
    """Map every decoded character back to its complete source span."""
    text, positions, cursor = [], [], 0
    for entity in re.finditer(r'&(?:#[xX][0-9a-fA-F]+|#\d+|[A-Za-z][A-Za-z0-9]+);', raw):
        for i in range(cursor, entity.start()):
            text.append(raw[i]); positions.append((i, i + 1))
        decoded = html.unescape(entity.group())
        for char in decoded:
            text.append(char); positions.append((entity.start(), entity.end()))
        cursor = entity.end()
    for i in range(cursor, len(raw)):
        text.append(raw[i]); positions.append((i, i + 1))
    return ''.join(text), positions


def _require(ok, message):
    if not ok:
        raise JustificationError(message)


def validate_bank(bank, code):
    _require(bank.get('version') == 1, 'Version de banque non prise en charge.')
    _require(bank.get('course', {}).get('code') == code, 'Code de cours incohérent.')
    entries = bank.get('entries')
    _require(isinstance(entries, list) and bool(entries), 'Banque vide ou invalide.')
    ids = []
    for entry in entries:
        ident = entry.get('id', '')
        _require(isinstance(ident, str) and re.fullmatch(re.escape(code.lower()) + r'-j-[a-z0-9-]+', ident), 'Identifiant invalide : ' + str(ident))
        ids.append(ident)
        for key in ('title', 'implication'):
            _require(isinstance(entry.get(key), str) and bool(entry[key].strip()), ident + ' : ' + key + ' absent.')
        for key in ('explanation', 'mechanism', 'limits'):
            _require(isinstance(entry.get(key), list) and (key == 'limits' or bool(entry[key])) and all(isinstance(x, str) and x.strip() for x in entry[key]), ident + ' : ' + key + ' invalide.')
        _require(isinstance(entry.get('match'), list) and bool(entry['match']), ident + ' : cibles absentes.')
        for match in entry['match']:
            _require(isinstance(match, dict), ident + ' : cible invalide.')
            for key in ('file', 'anchor', 'text'):
                _require(isinstance(match.get(key), str) and bool(match[key]), ident + ' : cible sans ' + key)
            _require(Path(match['file']).name == match['file'] and match['file'].startswith(code + '_') and match['file'].endswith('.html'), ident + ' : chemin de cible invalide.')
            if 'occurrence' in match:
                _require(type(match['occurrence']) is int and match['occurrence'] > 0, ident + ' : occurrence invalide.')
        _require(isinstance(entry.get('sources'), list) and bool(entry['sources']), ident + ' : sources absentes.')
        for source in entry['sources']:
            _require(isinstance(source, dict) and isinstance(source.get('title'), str) and source['title'].strip(), ident + ' : titre de source absent.')
            _require(isinstance(source.get('url'), str), ident + ' : URL source invalide.')
            url = urlsplit(source['url'])
            _require(url.scheme == 'https' and bool(url.netloc) and not url.username and not url.password, ident + ' : URL source invalide.')
    _require(len(ids) == len(set(ids)), 'Identifiants dupliqués dans la banque.')
    return entries


def render_templates(entries):
    esc = html.escape
    out = []
    for entry in entries:
        ident = entry['id']
        parts = ['<template data-pop="' + esc(ident, quote=True) + '" data-title="' + esc(entry['title'], quote=True) + '">', '<div class="mc-justification">']
        parts += ['<p>' + esc(x) + '</p>' for x in entry['explanation']]
        parts += ['<h4>Mécanisme physiopathologique</h4><ol>']
        parts += ['<li>' + esc(x) + '</li>' for x in entry['mechanism']]
        parts += ['</ol><h4>Conséquence clinique</h4><p>' + esc(entry['implication']) + '</p>']
        if entry['limits']:
            parts += ['<h4>Limites et contexte</h4>']
            parts += ['<p>' + esc(x) + '</p>' for x in entry['limits']]
        parts += ['<h4>Sources</h4><ul data-justification-sources="1">']
        parts += ['<li><a href="' + esc(x['url'], quote=True) + '" target="_blank" rel="noopener noreferrer">' + esc(x['title']) + '</a></li>' for x in entry['sources']]
        parts += ['</ul></div></template>']
        out.append(''.join(parts))
    return '\n'.join(out)


def compile_bank(bank, sources, code=None):
    code = code or bank.get('course', {}).get('code')
    entries = validate_bank(bank, code)
    nodes = {name: _text_nodes(value) for name, value in sources.items()}
    patches = {name: [] for name in sources}
    matches = []
    for entry in entries:
        ident = entry['id']
        _require(not any(re.search(r'data-(?:pop|k)=["\']' + re.escape(ident) + r'["\']', source) for source in sources.values()), ident + ' : identifiant déjà utilisé.')
        for match in entry['match']:
            name, anchor, text = match['file'], match['anchor'], match['text']
            _require(name in sources, ident + ' : fichier absent ' + name)
            found = []
            for node in nodes[name]:
                if anchor not in node['ancestors']:
                    continue
                visible, offsets = _decoded_positions(sources[name][node['start']:node['end']])
                pattern = re.escape(text)
                if text[0].isalnum() or text[0] == '_': pattern = r'(?<!\w)' + pattern
                if text[-1].isalnum() or text[-1] == '_': pattern += r'(?!\w)'
                for hit in re.finditer(pattern, visible):
                    start = node['start'] + offsets[hit.start()][0]
                    end = node['start'] + offsets[hit.end() - 1][1]
                    found.append((start, end))
            occurrence = match.get('occurrence')
            _require(bool(found), ident + ' : texte natif introuvable sous ' + anchor + ' : ' + text)
            if occurrence is None:
                _require(len(found) == 1, ident + ' : cible ambiguë (' + str(len(found)) + '), occurrence explicite requise.')
                start, end = found[0]
            else:
                _require(occurrence <= len(found), ident + ' : occurrence hors limites.')
                start, end = found[occurrence - 1]
            _require(not any(start < b and end > a for a, b, unused in patches[name]), ident + ' : cibles superposées.')
            raw = sources[name][start:end]
            button = '<button class="w" data-k="' + html.escape(ident, quote=True) + '" data-justification="1">' + raw + '</button>'
            patches[name].append((start, end, button))
            matches.append(dict(match, id=ident, start=start, end=end))
    transformed = dict(sources)
    for name, changes in patches.items():
        for start, end, replacement in sorted(changes, reverse=True):
            transformed[name] = transformed[name][:start] + replacement + transformed[name][end:]
    report = {'code': code, 'course': bank['course'], 'entries': len(entries), 'windows': len(entries), 'targets': len(matches), 'matches': matches, 'exhaustive_review': False}
    return transformed, render_templates(entries), report


def load_course_justifications(code, chapter_dir):
    folder = Path(chapter_dir)
    path = folder / (code + '_justifications.json')
    if not path.exists():
        return None
    bank = json.loads(path.read_text(encoding='utf-8'))
    sources = {p.name: p.read_text(encoding='utf-8') for p in sorted(folder.glob('*.html'))}
    return compile_bank(bank, sources, code)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--course', action='append')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    codes = args.course or sorted(p.parent.name for p in (args.root / 'chapters').glob('*/*_justifications.json'))
    reports = []
    for code in codes:
        result = load_course_justifications(code, args.root / 'chapters' / code)
        if result:
            reports.append(result[2])
    print(json.dumps({'courses': len(reports), 'windows': sum(r['windows'] for r in reports), 'targets': sum(r['targets'] for r in reports), 'reports': reports, 'exhaustive_review': False}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
