#!/usr/bin/env python3
"""Reproducible OFS import: labels/codes only, no inclusion or clinical prose."""
import csv
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from fragment_surface import frontend_catalog
from nosologyEngine import sha256


def expand(spec, available):
    result = set()
    for part in spec.split():
        if '-' in part:
            first, last = part.split('-')
            result.update(code for code in available if first <= code <= last)
        elif part in available:
            result.add(part)
    return result


def main():
    full, original, courses = frontend_catalog(ROOT)
    old = {item['code']: item for item in full['entries']}
    fragment_by_system = {system: fragment['id'] for fragment in json.loads((ROOT / 'fragments.json').read_text())
                          for system in fragment['rattachements'] if len(system) != 3}
    source = ROOT / 'nosology/sources'
    xml_archive = source / 'ofs-cim10gm2024-fr-claml.zip'
    csv_archive = source / 'ofs-cim10gm2024-fr-csv.zip'
    with zipfile.ZipFile(xml_archive) as archive:
        xml = archive.read(next(name for name in archive.namelist() if name.endswith('.xml')))
    root = ET.fromstring(xml)
    classes = {item.get('code'): item for item in root.findall('Class')}
    chapters = [item.get('code') for item in root.findall('Class') if item.get('kind') == 'chapter']
    def title(item):
        label = item.find("Rubric[@kind='preferred']/Label")
        return ' '.join(''.join(label.itertext()).split()) if label is not None else ''
    blocks = {code: {'title': title(item), 'parent': item.find('SuperClass').get('code')}
              for code, item in classes.items() if item.get('kind') == 'block'}
    def category_block(code):
        parent = classes[code].find('SuperClass').get('code')
        return parent
    with zipfile.ZipFile(csv_archive) as archive:
        raw = archive.read(next(name for name in archive.namelist() if '_codes_' in name))
    rows = list(csv.reader(io.StringIO(raw.decode('utf-8-sig')), delimiter=';'))
    entities = []
    for row in rows:
        code = row[6]; chapter = chapters[int(row[3]) - 1]
        excluded = 'Psychisme exclu' if code.startswith('F') or code.startswith('U63') else (
            'Code non affecté OFS (Content=N)' if row[19] == 'N' else None)
        parent = code[:-1] if len(code) == 6 else code[:3] if len(code) > 3 else None
        entities.append({'code': code, 'title': row[8], 'chapter': chapter,
                         'block': category_block(code[:3]), 'parent': parent,
                         'marker': ''.join(mark for mark in ('!', '*', '†') if mark in row[5]),
                         'terminal': row[1] == 'T', 'excluded': excluded})
    active = {item['code'] for item in entities if not item['excluded'] and len(item['code']) == 3}
    if active != set(old):
        raise ValueError('Le catalogue de base et les catégories actives OFS divergent.')
    mappings = {code: {'fragment': original[code], 'basis': 'spécialité du catalogue existant'} for code in active}
    def assign(spec, ident, basis):
        for code in expand(spec, active):
            mappings[code] = {'fragment': ident, 'basis': basis}
    # Localised tumours and congenital anomalies follow their organ, while
    # systemic/unknown tumours and multisystem syndromes remain in T4.
    for code in active:
        if code.startswith(('C', 'Q')) or code.startswith('D') and code <= 'D48':
            organ = fragment_by_system.get(old[code].get('system'))
            if organ and organ != 'T4':
                mappings[code] = {'fragment': organ, 'basis': 'localisation anatomique du catalogue, code OFS vérifié'}
    for spec, ident in [
        ('C00-C14 C30-C32 Q30-Q31 Q35-Q38', 'S12'),
        ('C64-C66 Q60-Q63', 'S04'), ('Q64', 'S15'), ('Q83', 'S14'),
        ('R07 R09', 'S02'), ('R54', 'T2'), ('R70-R94', 'T5'),
        ('Z02 Z04 Z53', 'T7'), ('Z01', 'T5'), ('Z08 Z12 Z51 Z80 Z85', 'T4'),
        ('Z20-Z22', 'T1'), ('Z30-Z31', 'S14'), ('Z32-Z39', 'S16'),
        ('Z47 Z89', 'S10'), ('Z49', 'S04'), ('Z54 Z74', 'T2'), ('Z88', 'S07'), ('Z95', 'S01'),
        ('U50-U51 U53-U54', 'T2'), ('U52', 'S10'), ('U55', 'T3'), ('U69', 'T5'),
        ('S00-S03 S07-S08 S10-S11 S13 S15-S16', 'S12'), ('S04 S06 S14', 'S08'), ('S05', 'S13'),
        ('S12 S22 S32 S42 S43 S46 S52 S53 S56 S62-S63 S66 S72-S73 S76 S82-S83 S86 S92-S93 S96', 'S10'),
        ('S20-S21 S23 S25 S27 S29', 'S02'), ('S24 S34 S44 S54 S64 S74 S84 S94', 'S08'),
        ('S26 S35 S45 S55 S65 S75 S85 S95', 'S01'), ('S30-S31 S36', 'S03'), ('S37', 'S04'),
        ('S41 S51 S61 S71 S81 S91 T20-T25 T29-T32 T33-T35', 'S11'),
        ('T15 T26', 'S13'), ('T16-T17', 'S12'), ('T18 T28', 'S03'), ('T19', 'S15'), ('T27', 'S02'),
    ]:
        assign(spec, ident, 'répartition transversale par système ; rattachement administratif explicite')
    # Preserve canonical course ownership and every existing alias.
    for course in courses.values():
        for code in set(course['covers']) | {course['code']}:
            if code in mappings:
                mappings[code] = {'fragment': course['source_fragment_id'], 'basis': 'cours existant conservé, sans déplacement'}
    # Relations to other specialties are links, not duplicate course shells.
    for code, mapping in mappings.items():
        secondary = set()
        anatomical = fragment_by_system.get(old[code].get('system'))
        if anatomical:
            secondary.add(anatomical)
        if code[0] in 'CQ' or code[0] == 'D' and code <= 'D48': secondary.add('T4')
        if code[0] in 'STVWXY': secondary.add('T3')
        if code[0] in 'AB': secondary.add('T1')
        infectious = classes[code].find("Meta[@name='Infectious']")
        if infectious is not None and infectious.get('value') == 'J': secondary.add('T1')
        if code[0] == 'R': secondary.add('T5')
        if code[0] == 'Z': secondary.add('T6')
        secondary.discard(mapping['fragment'])
        mapping['secondary_fragments'] = sorted(secondary)
    for spec, related in [('R07 R09', ['S01', 'S12']), ('R04', ['S12']),
                          ('S37', ['S14', 'S15']), ('T27', ['S12']), ('T28', ['S12', 'S14', 'S15']),
                          ('Z31', ['S15']), ('Z51', ['T3']), ('Z43 Z45 Z46 Z90 Z93 Z94 Z96 Z99',
                           ['S01', 'S02', 'S03', 'S04', 'S10', 'S13', 'S14', 'S15'])]:
        for code in expand(spec, active):
            mappings[code]['secondary_fragments'] = sorted((set(mappings[code]['secondary_fragments']) | set(related)) - {mappings[code]['fragment']})
    # Source evidence is the federal-exam framework in force in 2026. SSPs
    # are presentations, not an official ICD disease checklist. The explicit
    # mapping below is pedagogical and is never described as an official table.
    pdf = source / 'profiles2017.pdf'
    text = subprocess.check_output(['pdftotext', '-layout', str(pdf), '-'], stderr=subprocess.DEVNULL).decode()
    ssps = {int(n): label.strip() for n, label in re.findall(r'^\s*SSP\s+(\d+)\s+(.+)', text, re.M)}
    if set(ssps) != set(range(1, 266)): raise ValueError('PROFILES 2017 : 265 SSP attendus.')
    rules = [
        ('I00-I09 I30-I43', [44, 133]), ('I10-I15 I95', [131, 214]),
        ('I20-I25', [44, 151, 204]), ('I26-I28 J80 J96', [46, 206]),
        ('I44-I49', [50, 137, 155, 218]), ('I50-I52', [12, 46, 146]),
        ('I60-I69 G45', [103, 205]), ('I70-I79', [85, 144]), ('I80-I89', [12, 146]),
        ('J00-J06 J30-J39', [19, 30, 31, 35, 49]), ('J09-J22', [6, 45, 46]),
        ('J40-J47 J60-J70 J82-J86', [45, 46, 49]), ('J90-J94', [46, 167]), ('J95 J98 J99', [41, 46]),
        ('A00-A09', [59, 157]), ('A15-A19', [6, 45]), ('A40-A41', [6, 214]),
        ('A50-A64 B20-B24 Z20-Z22', [253]), ('B15-B19 K70-K77', [91, 160]),
        ('A80-A89 G00-G09', [6, 101, 207]), ('B50-B54', [6, 242]),
        ('K00-K14', [25, 27]), ('K20-K31', [47, 48, 52, 210]), ('K35-K38', [52, 203]),
        ('K40-K46', [73]), ('K50-K52 K90', [59]), ('K55-K67', [52, 55, 58, 60]),
        ('K80-K87', [52, 91, 203, 209]), ('K92', [60, 210]),
        ('E00-E07', [37, 163]), ('E10-E14', [3, 158]), ('E40-E46 E50-E64', [16, 138, 170]),
        ('E20-E35', [156, 184]), ('E84', [46, 189]), ('E85', [146, 173]),
        ('E65-E68', [15]), ('E70-E77', [264]), ('E78', [162]), ('E86-E87', [156]),
        ('G20-G26', [98]), ('G30-G32', [102, 139]), ('G35-G37', [103, 104]),
        ('G40-G41', [105, 219]), ('G43-G44', [101]), ('G47', [11, 40]),
        ('G50-G64', [85, 104]), ('G70-G73', [103, 194]), ('G80-G83', [103]), ('G90-G99', [103, 104]),
        ('N00-N19', [63, 161, 164, 173]), ('N20-N23', [64, 209]), ('N25-N39', [64, 76, 77]),
        ('N40-N51', [71, 72, 75, 77]), ('N60-N64', [42]), ('N70-N77', [68, 80, 253]),
        ('N80-N98', [65, 66, 67, 68, 74, 78, 79]),
        ('D50-D64', [147, 165]), ('D65-D69', [88, 152, 174]), ('D70-D77', [154, 171]),
        ('D80-D89', [247]), ('M30-M36', [86, 168]), ('T78', [37, 49, 87, 263]),
        ('M00-M25', [86]), ('M40-M54', [81, 82, 83]), ('M60-M79', [84, 85]), ('M80-M85', [169]),
        ('L00-L08 L80-L99', [90, 93, 95]), ('L10-L14', [93]), ('L20-L30 L50-L54', [9, 93]),
        ('L40-L45', [93, 95]), ('L60-L75', [92, 94]), ('L89', [200]),
        ('H00-H22', [33, 38]), ('H25-H36 H40-H48', [18, 39]), ('H49-H52', [17, 36, 39]),
        ('H53-H54', [18, 39]), ('H60-H75', [24, 26, 28]), ('H80-H95', [28, 100]),
        ('O00-O08', [79, 182, 183]), ('O10-O99', [178, 179, 181]), ('O80-O84', [176, 179]),
        ('P00-P04', [190]), ('P05-P08', [175]), ('P10-P96', [175, 190, 194]),
        ('S00-S09', [112]), ('S10-S19', [115]), ('S20-S29', [116]), ('S30-S39', [106]),
        ('S40-S99', [113, 220]), ('T00-T14', [108, 114, 220]), ('T15-T19', [111]),
        ('T20-T35', [107, 208]), ('T36-T65', [211, 263]), ('T66-T75', [107, 110, 211]),
        ('T80-T88', [250, 263]), ('Z00 Z01 Z10', [224]), ('Z02 Z04', [258]),
        ('Z08 Z11-Z13', [225, 226]), ('Z23-Z28', [187, 222]), ('Z30', [69]), ('Z31', [65]),
        ('Z32-Z39', [176, 177, 180, 181, 183]), ('Z49 Z50', [255]), ('Z51', [229, 230, 231]),
        ('Z52 Z94', [261]), ('Z53', [251, 252]), ('Z54 Z74', [197, 201]), ('Z55-Z65', [233, 235, 238, 241]),
        ('Z71 Z72', [223, 244, 256]), ('Z88', [263]),
        ('R00', [137]), ('R01', [133]), ('R02', [144]), ('R03', [131]), ('R04 R05', [45]),
        ('R06', [41, 46, 49]), ('R07', [35, 44, 51]), ('R09', [140]), ('R10', [52]),
        ('R11', [61]), ('R12', [47]), ('R13', [48]), ('R14', [53]), ('R15', [55, 202]),
        ('R16 R18 R19', [54, 167]), ('R17', [91]), ('R20', [104]), ('R21 R23', [93, 95]),
        ('R22', [2]), ('R25-R29', [96, 97, 98, 103]), ('R30-R36', [63, 64, 75, 76, 77]),
        ('R40', [145, 217]), ('R41', [102, 126, 139]), ('R42', [100]), ('R47-R49', [19, 99]),
        ('R50', [6]), ('R51', [101]), ('R52', [10]), ('R53', [4]), ('R54', [197, 201]),
        ('R55', [149, 217]), ('R56', [105, 219]), ('R57', [214]), ('R58', [215]),
        ('R59', [2]), ('R60', [12, 146]), ('R61', [1]), ('R62', [184, 188]), ('R63', [3, 15, 16]),
        ('R64', [138]), ('R68', [5]), ('R70', [168]), ('R71', [165]), ('R72', [154]),
        ('R73', [158]), ('R74', [151, 160]), ('R77', [172]), ('R79', [156, 162]),
        ('R80', [173]), ('R81', [158]), ('R82', [164]), ('R85', [157]), ('R90-R93', [153]),
        ('R95', [191]), ('R96', [14]),
        ('Q00-Q99', [70, 177]), ('C00-C97', [159, 227]),
    ]
    exam_mapping = {}
    for spec, numbers in rules:
        for code in expand(spec, active):
            exam_mapping[code] = sorted(set(exam_mapping.get(code, [])) | set(numbers))
    data = {'version': 'CIM-10-GM 2024', 'language': 'fr', 'publisher': 'OFS',
            'sources': {
                'csv': {'url': 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/32686265/master', 'sha256': sha256(csv_archive)},
                'claml': {'url': 'https://dam-api.bfs.admin.ch/hub/api/dam/assets/32686264/master', 'sha256': sha256(xml_archive)},
                'profiles': {'url': 'https://www.siwf.ch/files/pdf24/profiles_2017-broschuere.pdf', 'sha256': sha256(pdf)}},
            'chapters': {code: {'title': title(classes[code])} for code in chapters},
            'blocks': blocks, 'entities': entities, 'mapping': dict(sorted(mappings.items())),
            'exam_mapping': dict(sorted(exam_mapping.items())), 'ssp_labels': ssps,
            'exam_mapping_status': 'Mapping pédagogique explicite, pas de table officielle CIM/PROFILES. Sans lien établi : à arbitrer, jamais déclaré non exigible.'}
    (ROOT / 'nosology/reference.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
    chapter_summary = {code: {'title': title(classes[code]), 'fragments': set(), 'excluded_categories': []} for code in chapters}
    block_summary = {code: {'title': item['title'], 'fragments': set(), 'categories': []} for code, item in blocks.items()}
    for entity in entities:
        if len(entity['code']) != 3: continue
        if entity['excluded']:
            chapter_summary[entity['chapter']]['excluded_categories'].append({'code': entity['code'], 'reason': entity['excluded']})
            continue
        mapping = mappings[entity['code']]
        associated = {mapping['fragment'], *mapping['secondary_fragments']}
        chapter_summary[entity['chapter']]['fragments'].update(associated)
        block_summary[entity['block']]['fragments'].update(associated)
        block_summary[entity['block']]['categories'].append(entity['code'])
    for table in (chapter_summary, block_summary):
        for item in table.values(): item['fragments'] = sorted(item['fragments'])
    (ROOT / 'nosology/mapping_summary.json').write_text(json.dumps({'chapters': chapter_summary, 'blocks': block_summary}, ensure_ascii=False, indent=2) + '\n')
    print(len(active), 'catégories actives ;', sum(not item['excluded'] for item in entities), 'codes actifs hors psychisme.')


if __name__ == '__main__': main()
