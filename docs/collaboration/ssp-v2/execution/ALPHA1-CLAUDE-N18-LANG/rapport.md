# Audit linguistique agressif — N18 Maladie rénale chronique (Alpha, tour 1)

Mission ALPHA1-CLAUDE-N18-LANG · génération 1 · branche `claude/alpha1/n18-lang-g1` · base `f664dd9e8da71f647dd3dc4da18f509f8517959c` · conversation `alpha1-claude-n18-lang` · exécution par un sous-agent Claude Code (modèle et effort conformes au manifeste).

> Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.

## 1. Ce que dit ce rapport en deux phrases

Le texte de N18 est propre sur le plan orthographique (une seule coquille avérée : « arrondi à2,5 »), mais il souffre de trois défauts répétés : des énumérations télégraphiques sans articles (122 corrections), des infinitifs ou des phrases nominales que le guide de rédaction proscrit (45 corrections), et une typographie française absente (aucune espace insécable dans les six fichiers, environ 2 000 occurrences concernées). Le lot livre 331 propositions locales prêtes à appliquer, 10 règles typographiques mécaniques et 6 renvois médicaux ; aucun fait, chiffre, dose ou source n’est modifié.

## 2. Méthode et garanties

1. **Entrée.** Les empreintes SHA-256 des 7 fichiers (`N18_a`, `_b`, `_c`, `_d`, `_pop1`, `_pop2`, `glossary/n18.py`) ont été recalculées et comparées au manifeste : 7 sur 7 conformes. La base du manifeste (`bfc4576b…`) est un ancêtre direct du worktree (`f664dd9e…`).
2. **Lecture.** Les 7 fichiers ont été lus en entier, y compris les tableaux, légendes, fenêtres, encadrés « À retenir », critères formels (`div.alert`) et paramètres clés (`div.key`). Les attributs `alt` et `data-title` ont été relus ; les libellés des paragraphes « Sources : » aussi (liens non suivis).
3. **Contrôle mécanique.** Pour chacune des 331 propositions, l’extrait `ancien` apparaît **exactement une fois** dans le fichier brut ; aucun recouvrement n’existe entre deux extraits d’un même fichier ; l’application simulée de l’ensemble conserve le décompte de chaque balise HTML dans les 6 fichiers. Un contrôle des nombres confirme qu’aucun chiffre ne change, sauf trois ajouts d’unité ou d’équivalence exacte (A04 « 55 à 35 mL/min/1,73 m² », A07 « 25 mL/min/1,73 m² », A08 « 10–11,5 g/dL (soit 100–115 g/L) »).
4. **Périmètre.** Aucune affirmation médicale n’a été vérifiée contre une source : toute reformulation susceptible de déplacer un sens médical est marquée `renvoi_medical` et n’est pas proposée.

## 3. Tableau de bord

| Indicateur | Valeur |
|---|---|
| Propositions locales (`propositions.json`) | 331 |
| Renvois médicaux (sans reformulation) | 6 |
| Règles typographiques globales (`regles_typographiques.json`) | 10 |
| Constats sans proposition (`rapport.json`) | 10 |
| Répartition par fichier | A : 33 · B : 69 · C : 42 · D : 26 · fenêtres 1 : 103 · fenêtres 2 : 58 |
| Articles omis devant une énumération | 122 |
| Ambiguïtés levées | 35 |
| Ponctuation et typographie locales | 33 |
| Grammaire, accords | 34 |
| Infinitifs injonctifs et phrases nominales | 45 |
| Lourdeurs, registre, métaphores | 29 |
| Anglicismes | 13 |
| Terminologie, cohérence, abréviation | 10 |

## 4. Constats par catégorie (du plus gênant au moins gênant)

### 4.1 Énumérations sans articles et phrases télégraphiques (122 + 22 propositions)

Le défaut dominant. Exemple (A05 §1) : « L’entretien recherche dates des premières anomalies, épisodes aigus, diabète, hypertension… » devient « L’entretien recherche les dates des premières anomalies, les épisodes aigus, le diabète… ». La proposition respecte le §2 du guide (« le lecteur comprend, il ne devine pas »). Les fenêtres de pharmacologie en sont les plus atteintes (« Rechercher hypovolémie, déshydratation… Suivre poids, symptômes… »).

### 4.2 Infinitifs injonctifs (23 propositions)

Le guide les proscrit partout, cellules comprises. Les fenêtres Ramipril, Lasix, Néphrotrans, Venofer et Aranesp alternent phrases complètes et infinitifs (« débuter selon la FI à 1,25 mg oral… ») ; les reformulations passent à « on débute… » ou au passif. Quarante-trois cellules de tableau commencent encore par un infinitif d’action : dix ont été reformulées, les autres relèvent d’une convention d’intégration (constat K06).

### 4.3 Ambiguïtés (35 propositions) et accords (6)

Cas notables : « Dans ce cas, une anomalie de filtration… persistent au-delà de trois mois » (A01 §2), dont la logique contredit la phrase précédente ; « G3 ou plus ou après antécédent d’hyperkaliémie » (A07, P02, Ramipril), à comprendre « à partir de la catégorie G3 » ; « La polykystose… récemment immunosupprimées étaient exclues » (P01), où l’adjectif accorde des maladies avec un état de patient ; « la FI de Kerendia… atteint 60 » devenu « est d’au moins 60 » ; accord de verbe avec trois sujets coordonnés par « ou » (six cas).

### 4.4 Anglicismes et calques (13 propositions)

« 5 mg oral » (plusieurs occurrences, remplacé par « par voie orale » ; de même « sous-cutané »), « spot urinaire » (deux), « gold standard », « panel », « mal adaptative », « référer » (calque de *to refer*), « sur la vie » (de *lifetime*), « et/ou ».

### 4.5 Registre, métaphores et méta-discours (15 propositions)

« Vieillissement de la maladie », « tuyau perforé », « la clinique vérifie », « effondrent l’exposition », « cas fil rouge », ainsi que deux phrases qui parlent du plan du cours (« Le passage consacré à N18.80 porte sur… », proscrit par le §3 du guide).

### 4.6 Coquilles, ponctuation et typographie locales (34 propositions)

- « arrondi à2,5 » (coquille avérée, fenêtre Conversions) ;
- signes `<`, `>`, `≥`, `≤` collés aux nombres dans une quinzaine de cellules de tableau (« &lt;3 », « ≥60 ») alors que d’autres cellules du même tableau écrivent « &lt; 15 » ;
- « (Avril 2023.) » : point parasite à l’intérieur de la parenthèse d’une référence (cinq occurrences) ;
- formules sans espaces (« 0,8×70=56g », « kg×(140−âge en années)/(72× ») ;
- titre de fenêtre « crédible? » sans espace avant « ? ».

## 5. Règles typographiques globales (`regles_typographiques.json`)

Le dépôt n’emploie nulle part l’espace insécable (U+00A0 : 0 occurrence). Ces règles mécaniques couvrent donc des centaines de sites qu’un `ancien` unique ne peut pas désigner un à un.

| Règle | Occurrences |
|---|---|
| T1 — espace insécable avant « ; » (mélange de « m²; » et « … ; ») | 423 |
| T2 — espace insécable avant « : » | 326 |
| T3 — espace insécable avant « ? » | 28 |
| T4 — espaces insécables dans les guillemets « » | 29 paires |
| T5 — espace insécable entre nombre et unité (mL, mmol, %, kg…) | ≈ 1 040 |
| T6 — séparateur des milliers (« 4 304 », « 1 500 ») | 17 |
| T7 — « CO2 » → « CO₂ » | 3 |
| T8 — « /j » et « /jour » mêlés | 13 contre 18 |
| T9 — « et/ou » en prose | 4 |
| T10 — mois en majuscule dans les références (« Août 2026 ») | 181 |

## 6. Renvois médicaux (6, sans reformulation)

| Renvoi | Fichier | Question posée à l’audit médical |
|---|---|---|
| R01 | pop1 (rein normal) | Latéralité : « le droit souvent un peu plus que le gauche » est-il dans Hansen 2016 ? |
| R02 | pop1 (protéinurie) | Zone 50–60 % d’albumine non couverte entre « plus de 60 % » et « moins de 50 % » |
| R03 | a (A06) | « le jour même » et « le délai compte en jours » se contredisent-ils ? |
| R04 | d (P02 §4) | « Risque… d’accumulation change » : accumulation de quoi, et dans quel sens ? |
| R05 | d (tableau P02) | Coordination « jusqu’à stabilité, pression et fer » dans la ligne Aranesp |
| R06 | pop1 (grille G×A) | « Traiter et orienter » et « Traiter et référer » : deux libellés pour *Refer* et *Refer\** ? |

## 7. Constats sans proposition (détail dans `rapport.json`)

- **K01 — quinze sigles sans clé de glossaire** : SSED (48 occurrences), HUG (36), MAPA, LDL, IMC, ECG, ESH, ESC, FLOW, IRM, FIDELIO-DKD, FGF23, ATP, CRP, CYP2C8. Violation de la règle 3 de CLAUDE.md ; le glossaire est hors périmètre de ce lot.
- **K02 — textes dupliqués** : fenêtres Ganzoni (pop1) et Venofer (pop2) identiques ; 21 encadrés « À retenir » de pop2 répétés deux fois. Toute correction doit toucher les deux exemplaires (c’est fait pour Venofer/Ganzoni).
- **K03 — 36 introductions de tableau** de type « Le tableau rassemble… » contraires au §4 du guide.
- **K04 — cinq renvois identiques** « … permet de revoir les grandeurs et les limites de l’exemple », dont le sujet est un bouton.
- **K05 — S04 §6** : paragraphe de corrélations et trois encadrés qui le redoublent partiellement.
- **K06 — 43 cellules** à l’infinitif d’action.
- **K07 — 14 phrases de plus de 45 mots**, dont quatre coupées par proposition.
- **K08 — hémoglobine en g/dL et en g/L** dans les mêmes paragraphes.
- **K09 — variantes terminologiques** (référer/orienter, fiche suisse/fiche SSN, consensus diabète/consensus SSED/SSN, bloqueur/inhibiteur du système rénine–angiotensine).
- **K10 — absence de correcteur orthographique automatique** dans l’environnement.

## 8. Lacunes déclarées

1. Aucun correcteur orthographique (hunspell, aspell, enchant) n’était installé ; la vérification repose sur des balayages mécaniques et sur la relecture des 1 382 formes uniques. Une relecture avec LanguageTool ou Antidote reste nécessaire à l’intégration.
2. Aucune source médicale n’a été lue : ce lot ne vérifie pas le fond, il ne l’altère pas non plus. Deux reformulations reposent sur la lecture la plus naturelle du sens et sont signalées comme telles dans leur motif (A01 §2 ; fenêtre Créatinine, méthode de Jaffe).
3. Le glossaire n’a pas été modifié (écriture limitée au dossier d’exécution).
4. Les liens des paragraphes « Sources : » et les crédits des figures n’ont pas été vérifiés.
5. Vingt propositions comportent du balisage dans l’extrait `ancien` (cellules de tableau, titres, références) dont cinq s’appuient sur un identifiant `id="N18-C…"` : elles sont fragiles si la chaîne de build régénère les identifiants.

## 9. Livrables

- `propositions.json` : 337 entrées (331 propositions + 6 renvois médicaux à `nouveau: null`).
- `regles_typographiques.json` : 10 règles mécaniques avec expressions régulières et décomptes par fichier.
- `rapport.json` : rapport structuré (empreintes, synthèse, constats, lacunes).
- `rapport.md` : le présent document.

*Audit IA — revue distincte d’une validation médicale humaine ; aucune source canonique modifiée.*
