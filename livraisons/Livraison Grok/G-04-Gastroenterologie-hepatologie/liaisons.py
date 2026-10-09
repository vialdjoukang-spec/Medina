"""Connecteurs logiques et transitions (règle linguistique obligatoire du propriétaire).
Appliqués au HTML rendu de chaque îlot : paragraphes <p> sans classe et encadrés .alert.
Carte : {id_ilot: [[préfixe_phrase1, connecteur_phrase2, ...], ...]} par paragraphe.
Un préfixe qui se termine par « . » est une phrase de transition ajoutée avant le paragraphe ;
sinon c'est un connecteur suivi d'une virgule."""
import re
CAP = r'[A-ZÀÂÉÈÊÎÔÛÇ«]'
SPLIT = re.compile(r'(?<=[.?!])( )(?=(?:<b>)?' + CAP + ')')
LOWER = {'Le', 'La', 'Les', 'Un', 'Une', 'Il', 'Elle', 'Ils', 'Elles', 'Ce', 'Cette', 'Ces', 'Cet', 'Chez', 'Dans', 'Pour', 'Après', 'Sans', 'Si',
         'Selon', 'Leur', 'Leurs', 'Son', 'Sa', 'Ses', 'Plus', 'Aucun', 'Aucune', 'Chaque', 'Tout', 'Toute', 'Tous', 'On', 'En', 'Au', 'Aux', 'Du', 'Des',
         'De', 'Avec', 'Sous', 'Entre', 'Quand', 'Lorsque', 'Une', 'Cela', 'Parmi', 'Pendant', 'Avant', 'Hors', 'Seul', 'Seule', 'Elle', 'Neuf', 'Deux',
         'Trois', 'Quatre', 'Cinq', 'Six', 'Environ', 'Près', 'Sur', 'Par', 'Ni', 'Même', 'Le', 'À', 'Ici', 'Normalement', 'Exemple'}
PROPER = {'Helicobacter', 'Baveno', 'Forrest', 'Glasgow', 'Oakland', 'Child', 'Pylera', 'Suisse', 'Dieulafoy', 'Mallory', 'Zollinger', 'Boey',
          'Swissmedic', 'Barrett', 'Lyon', 'Los', 'Prague', 'Crohn', 'Savary', 'Montréal', 'Europe', 'Allemagne', 'Royaume', 'Rome', 'Vienne', 'Hinchey',
          'Ranson', 'Atlanta', 'Tokyo', 'Charcot', 'Murphy', 'Wilson', 'Gilbert', 'Whipple', 'Clostridioides', 'Escherichia', 'Salmonella', 'Campylobacter',
          'Shigella', 'Yersinia', 'Giardia', 'Lynch', 'Bristol', 'Montreal', 'Mayo', 'Harvey', 'Truelove', 'Alvarado', 'Lille', 'Maddrey', 'Marsh',
          'Schweiz', 'Pantozol', 'Nexium', 'Glypressine', 'Sandostatine', 'Gaviscon', 'Lugano', 'Bâle', 'Berne', 'Genève', 'Zurich', 'Lausanne'}
def _text_parts(html):
    """Découpe en phrases sans couper à l'intérieur d'une balise."""
    out, depth, last = [], 0, 0
    for m in SPLIT.finditer(html):
        pre = html[:m.start()]
        if pre.count('<') != pre.count('>'): continue
        if pre.count('(') > pre.count(')'): continue
        out.append(html[last:m.start()]); last = m.end()
    out.append(html[last:]); return out
def _join(conn, s):
    if not conn: return s
    if conn.endswith('.') or conn.endswith(':'): return conn + ' ' + s
    b = ''
    if s.startswith('<b>'): b, s = '<b>', s[3:]
    first = re.match(r"([A-Za-zÀ-ÿ’]+)", s)
    w0 = first.group(1) if first else ''
    base = w0.split('’')[0] if '’' in w0[:3] else w0
    if w0 and base not in PROPER and not re.search(r'[A-ZÀ-Þ]', w0[1:]) and w0[0].isupper():
        s = s[0].lower() + s[1:]
    sep = ' ' if re.search(r'(\bque|pourquoi|\bà|\bde)$', conn) else ', '
    return conn + sep + b + s
def sentences(html):
    return _text_parts(html)
def apply(body, plan):
    """body : HTML de l'îlot ; plan : liste par paragraphe (ordre d'apparition des <p> sans classe et des .alert)."""
    k = [0]
    def fix(inner):
        i = k[0]; k[0] += 1
        if i >= len(plan) or not plan[i]: return inner
        ss = _text_parts(inner); conns = plan[i]
        if len(conns) > len(ss): raise SystemExit('liaisons : trop de connecteurs (%d > %d) pour « %s »' % (len(conns), len(ss), re.sub('<[^>]+>', '', inner)[:80]))
        return ' '.join(_join(conns[j] if j < len(conns) else '', s) for j, s in enumerate(ss))
    def rp(m): return m.group(1) + fix(m.group(2)) + m.group(3)
    body = re.sub(r'(<p>|<div class="alert"><b>[^<]*</b> )(.*?)(</p>|</div>)', rp, body, flags=re.S)
    return body
def dump(body):
    k = 0; out = []
    for m in re.finditer(r'(<p>|<div class="alert"><b>[^<]*</b> )(.*?)(</p>|</div>)', body, re.S):
        ss = _text_parts(m.group(2))
        out.append('  P%d: ' % k + ' | '.join(' '.join(re.sub('<[^>]+>', '', s).split()[:5]) for s in ss)); k += 1
    return '\n'.join(out)

# ---- Termes interactifs systématiques (règle de précision et d'interactivité du propriétaire)
def _inside(body, pos):
    pre = body[:pos]
    if pre.rfind('<') > pre.rfind('>'): return True
    for tag in ('button', 'a', 'figcaption', 'th', 'small'):
        o = max(pre.rfind('<' + tag + ' '), pre.rfind('<' + tag + '>'))
        if o != -1 and pre.rfind('</' + tag + '>') < o: return True
    return False
def termes(body, terms):
    """terms : liste (motif regex, clé de fenêtre). Première occurrence par îlot, hors balises, boutons, liens et légendes."""
    for pat, key in terms:
        if 'data-k="' + key + '"' in body: continue
        for m in re.finditer(pat, body):
            if _inside(body, m.start()): continue
            body = body[:m.start()] + '<button class="w" data-k="' + key + '">' + m.group(0) + '</button>' + body[m.end():]
            break
    return body
