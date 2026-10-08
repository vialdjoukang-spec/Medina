#!/usr/bin/env python3
"""Rend un document de consignes Markdown simple (titres, listes, tableaux, gras) en PDF clair."""
import re, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem

D = '/usr/share/fonts/truetype/dejavu/'
pdfmetrics.registerFont(TTFont('Serif', D + 'DejaVuSerif.ttf'))
pdfmetrics.registerFont(TTFont('Serif-B', D + 'DejaVuSerif-Bold.ttf'))
pdfmetrics.registerFontFamily('Serif', normal='Serif', bold='Serif-B', italic='Serif', boldItalic='Serif-B')
INK, RED, GREEN = colors.HexColor('#1b1b1b'), colors.HexColor('#a3241c'), colors.HexColor('#1f3428')
body = ParagraphStyle('b', fontName='Serif', fontSize=9.6, leading=13.4, textColor=INK, alignment=4, spaceAfter=4)
h1 = ParagraphStyle('h1', parent=body, fontName='Serif-B', fontSize=15, leading=19, textColor=GREEN, alignment=0, spaceAfter=8)
h2 = ParagraphStyle('h2', parent=body, fontName='Serif-B', fontSize=11.5, leading=15, textColor=RED, alignment=0, spaceBefore=8, spaceAfter=4)
cell = ParagraphStyle('c', parent=body, fontSize=8.2, leading=10.6, alignment=0, spaceAfter=0)

def inline(t):
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'`(.+?)`', r'<font face="Serif-B" color="#1f3428">\1</font>', t)
    return re.sub(r'(?<![\w/])\*([^*/]+?)\*(?![\w/])', r'<i>\1</i>', t)

def render(src, out):
    story, bullets, rows = [], [], []
    def flush():
        nonlocal bullets, rows
        if bullets:
            story.append(ListFlowable([ListItem(Paragraph(inline(b), body), leftIndent=12) for b in bullets], bulletType='bullet', start='•', leftIndent=12))
            bullets = []
        if rows:
            data = [[Paragraph(inline(c), cell) for c in r] for r in rows if not re.fullmatch(r'[\s|:-]+', '|'.join(r))]
            t = Table(data, repeatRows=1, colWidths=[52*mm, 34*mm, 88*mm][:len(data[0])] if len(data[0]) == 3 else None)
            t.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), .4, colors.HexColor('#9aa5a0')),
                                   ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e7efe9')),
                                   ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
            story.extend([t, Spacer(1, 5)]); rows = []
    for line in open(src, encoding='utf-8').read().splitlines():
        s = line.strip()
        if s.startswith('|'):
            if bullets: flush()
            rows.append([c.strip() for c in s.strip('|').split('|')]); continue
        if rows: flush()
        if s.startswith('- '): bullets.append(s[2:]); continue
        flush()
        if s.startswith('# '): story.append(Paragraph(inline(s[2:]), h1))
        elif s.startswith('## '): story.append(Paragraph(inline(s[3:]), h2))
        elif s: story.append(Paragraph(inline(s), body))
    flush()
    def foot(c, d):
        c.saveState(); c.setFont('Serif', 7.5); c.setFillColor(colors.HexColor('#555555'))
        c.drawString(18*mm, 10*mm, 'MEDINA · Consignes communes Claude Code et Codex · 8 octobre 2026')
        c.drawRightString(192*mm, 10*mm, 'page %d' % d.page); c.restoreState()
    SimpleDocTemplate(out, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=16*mm, bottomMargin=16*mm,
                      title='MEDINA — Consignes du 8 octobre 2026', author='Dr Vial Tato Djoukang (consignes) ; mise en forme Claude Code').build(story, onFirstPage=foot, onLaterPages=foot)

if __name__ == '__main__':
    render(sys.argv[1], sys.argv[2])
