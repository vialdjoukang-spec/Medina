from images import Schema
S = Schema(600, 350, 'Classification de Forrest : stigmates endoscopiques de l’ulcère')
cells = [('Ia', 'Saignement en jet'), ('Ib', 'Suintement'), ('IIa', 'Vaisseau visible\nnon hémorragique'),
         ('IIb', 'Caillot adhérent'), ('IIc', 'Tache pigmentée\nplane'), ('III', 'Fond propre\n(fibrine)')]
risk = ['élevé', 'élevé', 'élevé', 'intermédiaire', 'faible', 'faible']
d = S.d
for i, (cl, lab) in enumerate(cells):
    col, row = i % 3, i // 3
    x0, y0 = 20 + col * 195, 40 + row * 145
    # muqueuse et cratère (coupe)
    d.line([(x0, y0 + 50), (x0 + 55, y0 + 50)], fill='#7a3b2e', width=4)
    d.line([(x0 + 125, y0 + 50), (x0 + 180, y0 + 50)], fill='#7a3b2e', width=4)
    d.arc([x0 + 55, y0 + 10, x0 + 125, y0 + 90], 0, 180, fill='#7a3b2e', width=4)
    d.chord([x0 + 59, y0 + 14, x0 + 121, y0 + 86], 0, 180, fill='#f2ead8')
    cx, cy = x0 + 90, y0 + 86
    if cl == 'Ia':
        for k in range(-2, 3):
            d.line([(cx, cy - 4), (cx + 6 * k, y0 - 2)], fill='#c0151a', width=3)
    if cl == 'Ib':
        for k in range(5):
            d.ellipse([cx - 30 + 13 * k, cy - 18, cx - 22 + 13 * k, cy - 8], fill='#c0151a')
    if cl == 'IIa':
        d.ellipse([cx - 9, cy - 22, cx + 9, cy - 4], fill='#7d1d24', outline='#3b0b0e', width=2)
    if cl == 'IIb':
        d.ellipse([cx - 28, cy - 34, cx + 28, cy - 2], fill='#3b0b0e')
    if cl == 'IIc':
        d.ellipse([cx - 14, cy - 12, cx + 14, cy - 3], fill='#4a2a1a')
    S.text(x0 + 90, y0 + 105, 'Forrest ' + cl, 13, bold=True, anchor='ma')
    S.text(x0 + 90, y0 + 122, lab, 11, anchor='ma')
    S.text(x0 + 158, y0 + 2, 'risque\n' + risk[i], 10, fill='#c0151a' if risk[i] == 'élevé' else '#555', anchor='ma')
print(S.save('K92', 'k92_forrest_schema.gif', 'Coupe schématique d’un ulcère gastroduodénal pour chacun des six stigmates de Forrest (Ia, Ib, IIa, IIb, IIc, III) et niveau de risque de récidive ; définitions selon ESGE 2021.'))
