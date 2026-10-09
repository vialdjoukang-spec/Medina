from images import Schema
S = Schema(600, 330, 'Profondeur de la lésion : érosion, ulcère, ulcère perforé')
d = S.d
layers = [('Muqueuse', '#e9b8a8', 40), ('Musculaire muqueuse', '#b4584a', 8), ('Sous-muqueuse', '#f3e2c6', 46), ('Musculeuse', '#c97a6a', 60), ('Séreuse', '#d9d0c0', 10)]
x0, x1, ytop = 130, 590, 70
y = ytop; ys = {}
for name, col, h in layers:
    d.rectangle([x0, y, x1, y + h], fill=col)
    ys[name] = (y, y + h)
    S.text(x0 - 6, y + h / 2 - 7, name, 11, anchor='ra')
    y += h
bottom = y
# trois colonnes de lésions
def crater(cx, depth, wtop):
    d.polygon([(cx - wtop, ytop), (cx + wtop, ytop), (cx + wtop * 0.45, depth), (cx - wtop * 0.45, depth)], fill='#ffffff', outline='#7a3b2e')
    d.line([(cx - wtop * 0.45, depth), (cx + wtop * 0.45, depth)], fill='#a0a0a0', width=3)  # fibrine
crater(205, ys['Muqueuse'][1] - 12, 28)
crater(360, ys['Sous-muqueuse'][1] - 6, 42)
d.ellipse([352, ys['Sous-muqueuse'][1] - 16, 368, ys['Sous-muqueuse'][1] - 2], fill='#9b1b22', outline='#4a0b0e')  # artère érodée
d.polygon([(495, ytop), (565, ytop), (538, bottom + 2), (522, bottom + 2)], fill='#ffffff', outline='#7a3b2e')
for cx, t1, t2 in [(205, 'Érosion', 'ne franchit pas la\nmusculaire muqueuse'), (360, 'Ulcère', 'atteint la sous-muqueuse ;\nartère érodée = hémorragie'), (530, 'Ulcère perforé', 'traverse toute la paroi ;\npneumopéritoine')]:
    S.text(cx, bottom + 14, t1, 13, bold=True, anchor='ma')
    S.text(cx, bottom + 32, t2, 10, anchor='ma')
S.text(30, 44, 'Lumière gastrique', 11, fill='#555')
print(S.save('K25', 'k25_profondeur_schema.gif', 'Coupe schématique de la paroi gastrique montrant la profondeur d’une érosion, d’un ulcère avec artère sous-muqueuse érodée et d’un ulcère perforé ; d’après les définitions histologiques classiques reprises par la WSES 2020 et la S2k 2023.'))
