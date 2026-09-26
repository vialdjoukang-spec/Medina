import re,glob,sys,os
S='/tmp/claude-0/-home-user-Medina/97fe1427-b13e-5037-b07d-5e697279cdac/scratchpad/consignes'
PART={'pe':('l’onglet 2, « Examens complémentaires » (panneau pE)','_c.html'),
      'ps':('l’onglet 3, « Sciences fondamentales » (panneau pS)','_c2.html'),
      'pp':('l’onglet 4, « Pharmacologie » (panneau pP)','_d.html')}
SPEC={'pe':"""Examens : pour chaque examen, explique la question clinique qu’il tranche, son principe physique ou biologique, ses valeurs normales (unité, population), les seuils qui changent la décision, sa sensibilité et sa spécificité quand elles sont connues, ses limites et ses pièges. Place les examens dans l’ordre du raisonnement (premier recours, puis examens de deuxième ligne). Introduis et commente chaque tableau. Garde au moins trois quiz au format de l’examen fédéral (au moins trois options, explication rédigée). Ajoute une figure quand une courbe ou un tracé aide à comprendre (courbe débit-volume, algorithme, images schématiques).""",
'ps':"""Sciences fondamentales : c’est la partie que le propriétaire juge la plus faible ; elle doit devenir la plus claire. Approfondis chaque discipline (anatomie, histologie, physiologie, biochimie ou immunologie, microbiologie ou génétique selon le cours) au niveau d’un cours universitaire, toujours relié à la maladie. Chaque discipline s’ouvre par une annonce qui dit quelle question clinique elle éclaire, expose le fonctionnement normal puis sa perturbation, contient au moins un schéma légendé (SVG noir et blanc) ou un tableau introduit et commenté, et se termine par des encadrés key de corrélation science → clinique, science → examen, science → traitement, en phrases complètes. Aucune liste de mots-clés ; aucun tableau posé sans introduction ni lecture.""",
'pp':"""Pharmacologie : annonce la logique thérapeutique (classes, place selon le stade et le phénotype, pourquoi tel choix avant tel autre) ; introduis et commente le tableau des doses (colonnes expliquées, lecture guidée, exemple de patient) ; conserve à l’identique chaque posologie vérifiée ; explique les interactions dangereuses dans un div.alert ; explique la surveillance et les effets indésirables par leur mécanisme ; rédige les monographies en fenêtres (mécanisme, essai nommé avec année et résultat, posologie conforme à l’information professionnelle suisse, effets indésirables, contre-indications, surveillance) en phrases complètes."""}
def keys(t): return re.findall(r'data-k="([^"]+)"',t)
for code in sys.argv[1:]:
    lc=code.lower();d=f'chapters/{code}'
    src={p:open(f'{d}/{code}{PART[p][1]}').read() for p in PART}
    tabA=open(f'{d}/{code}_a.html').read()+open(f'{d}/{code}_b.html').read()
    pops=''.join(open(f).read() for f in sorted(glob.glob(f'{d}/{code}_pop*.html')))
    defs=dict(re.findall(r'<template data-pop="([^"]+)"[^>]*>(.*?)</template>',pops,re.S))
    where={k:f for f in sorted(glob.glob(f'{d}/{code}_pop*.html')) for k in re.findall(r'data-pop="([^"]+)"',open(f).read())}
    seen=set(keys(tabA));own={}
    for p in ['pe','ps','pp']:
        ks=[k for k in dict.fromkeys(keys(src[p])) if k not in seen and k in defs];seen|=set(ks);own[p]=ks
    # fenêtres référencées seulement depuis d'autres fenêtres : pharmacologie
    rest=[k for k in defs if k not in seen and not k.startswith('pareto-')];own['pp']+=rest
    for p in PART:
        tab,fn=PART[p]
        lst='\n'.join(f'- {k} (dans {os.path.basename(where[k])})' for k in own[p]) or '- aucune'
        txt=f"""# Consigne de rédaction — chapitre {code}, {tab}

Projet MEDINA, dépôt /home/user/Medina : atlas de cours de médecine en français pour l’examen fédéral suisse. Le propriétaire, médecin, trouve le chapitre {code} trop difficile à suivre : trop de phrases nominales et d’infinitifs injonctifs, des parties ni annoncées ni conclues, des tableaux posés sans explication, des sciences fondamentales superficielles, une densité d’information trop faible. Son exigence : « le lecteur comprend, il ne devine pas ».

## Avant d’écrire
Lis en entier /home/user/Medina/docs/STYLE_REDACTION.md (obligatoire, il prime sur tes habitudes), puis PROMPT_MEDINA.md § 4, § 5, § 10, § 11, § 13, § 14, et CHAPTER_SPEC.md. Lis audits/{code}.md : la section « Vérification en texte intégral — 26.09.2026 » et la section « Réécriture pédagogique — 26.09.2026 » listent les données déjà vérifiées ; tu les conserves exactement (valeur, unité, source, année). Lis l’onglet 1, déjà réécrit (chapters/{code}/{code}_a.html et _b.html) : tu gardes ses seuils, son cas fil rouge et son vocabulaire, et tu évites les redites.

## Ta part, et elle seule
Tu réécris {tab} : le fichier chapters/{code}/{code}{fn}. D’autres rédacteurs réécrivent EN MÊME TEMPS les autres onglets du même chapitre. Tu ne touches à aucun autre fichier de chapitre, sauf ceux listés ci-dessous.
- Fichier principal : chapters/{code}/{code}{fn} (tu peux le réécrire en entier).
- Fenêtres nouvelles : crée chapters/{code}/{code}_pop_{p}.html et places-y toutes tes nouvelles fenêtres (<template data-pop="{lc}-…" data-title="…">…</template>).
- Fenêtres existantes dont tu es propriétaire (à réécrire selon le guide) :
{lst}
  Elles se trouvent dans des fichiers partagés avec les autres rédacteurs : tu les modifies UNIQUEMENT avec l’outil Edit (remplacement exact d’un bloc <template>…</template>), jamais avec Write, sed ou un script Python sur ces fichiers.
- Pareto : réécris la ou les fenêtres Pareto appelées par les boutons pareto-btn de ton onglet (même règle d’édition), avec des data-cover valides et une couverture de 5 à 20 % du texte.
- Glossaire : toute abréviation nouvelle va dans un fichier NOUVEAU glossary/{lc}_{p}.py, qui commence par la même ligne d’import que glossary/{lc}.py et utilise la même fonction a(...). Vérifie d’abord qu’une clé n’existe pas déjà : `cd /home/user/Medina && python3 -c "import build_medina as B; print(B.G.get('CLÉ'))"`. Si elle existe avec un autre sens, écris le terme en toutes lettres. N’ajoute jamais une clé existante.
- Journal des sources : consigne chaque donnée nouvelle (URL, date de consultation, valeur) dans le fichier NOUVEAU audits/{code}_reecriture_{p}.md.

## Exigences de contenu
{SPEC[p]}
Chaque îlot et chaque sous-partie h3 suit le guide : annonce (2 à 4 phrases), développement dense du normal au pathologique et du mécanisme à la décision, épilogue <div class="key"><b>À retenir.</b> …</div>. Chaque notion importante est un mot vert <button class="w" data-k="{lc}-cle">libellé</button> qui ouvre une fenêtre réelle, elle aussi rédigée en phrases complètes (intertitres div.lab suivis de phrases qui expliquent le pourquoi). Aucune condensation : tu n’enlèves aucune information exacte ; tu l’expliques et l’approfondis.

## Contrat HTML
Classes de la liste fermée seulement (alert card chap chap-body chap-head code fb ilot k key lab maj n next pager panel pareto-btn prev quiz ratio sci sci-bar sci-body src ssp status t tabs toc trap two ui w, plus small dans les fenêtres) ; aucun attribut style ; identifiants et clés préfixés « {lc}- » ; sous-parties <h3>n.m Titre</h3> ; figures <figure><svg viewBox … role="img" aria-label="…">…</svg><figcaption>Figure n — …</figcaption></figure> en noir et blanc. Les îlots gardent leurs identifiants (le plan nav.toc et les Pareto en dépendent) ; un nouvel îlot reçoit un identifiant nouveau et une entrée dans le plan de ton onglet. La structure du panneau (div.panel, sci-bar pour les sciences, pager) reste la même.

## Exactitude
Tolérance zéro. Toute donnée nouvelle est vérifiée dans la source primaire en ligne (swissmedicinfo.ch, compendium.ch, sociétés savantes, PubMed ou Europe PMC ; NEJM et JAMA renvoient 403 : passe par PubMed). Aucune métaphore, aucun jeu de mots, aucune formule de chantier.

## Discipline de travail en parallèle
Aucune commande git qui modifie l’état (commit, checkout, switch, stash, reset, restore, clean, merge, rebase) ; les lectures (git show, git diff, git log) sont permises. Tu ne lances ni build_front.py ni pack_v7.py. Travaille vite et bien : écris ton fichier principal en quelques grandes écritures plutôt qu’en centaines de petites.

## Contrôle final
`cd /home/user/Medina && python3 test_v7.py --static {code}` : aucune erreur ne doit concerner tes fichiers ni tes clés (des erreurs passagères peuvent venir des autres rédacteurs en cours ; cite-les sans y toucher). Relis ensuite ton texte une fois en traquant chaque phrase nominale et chaque infinitif injonctif, et corrige-les.

## Réponse finale
Un résumé bref : fichiers écrits, mots avant et après, fenêtres nouvelles et réécrites, données nouvelles sourcées, résultat du test, réserves.
"""
        open(f'{S}/{code}_{p}.md','w').write(txt)
        print(code,p,len(own[p]),'fenêtres possédées')
