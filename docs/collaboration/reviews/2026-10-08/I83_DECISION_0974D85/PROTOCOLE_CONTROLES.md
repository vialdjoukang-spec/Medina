# I83 — Varices des membres inférieurs : protocole de contrôles indépendants

Fragment propriétaire : **C-01-Cardiologie (S01)**. Remise à examiner :
`0974d854db292ae0311e435b3daea5fbed187e25`. Base de confiance :
`ea105ace0046c71492cc6a69ff4c61698ef2ce34`.

Ce protocole résulte de la lecture des scripts et de la vérification des outils.
**Aucune construction, aucun test du cours et aucun code de la remise entrante
n'ont été exécutés pour rédiger ce document.** Les commandes ci-dessous sont
vérifiées contre les interfaces du code ; leurs résultats restent à recueillir.
Le coordinateur prépare d'abord une copie complète et inspectée de la base,
puis y applique les seuls fichiers autorisés de la remise. Cette copie conserve
les compilateurs et scripts de contrôles de confiance.

## Outils effectivement présents

| Outil | Observation locale |
| --- | --- |
| Python | 3.12.14 ; module Python `playwright` présent |
| Node | v24.19.0 |
| Playwright Node | `/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.js` |
| Chromium | `/usr/bin/chromium`, exécutable présent |
| Découverte Node | `NODE_PATH` et `CODEX_PRIMARY_RUNTIME_NODE_MODULES` pointent vers les modules du runtime |

`tests/browser_runtime.cjs` reconnaît `MEDINA_CHROMIUM_PATH` et fournit les
arguments Linux du navigateur. Le script Python `test_v7.py` utilise la variable
distincte **`MEDINA_CHROMIUM`**. Une installation de dépendances n'est pas requise
avec les outils observés.

## Empreintes des scripts examinés

Les fichiers locaux ci-dessous sont identiques octet par octet aux blobs de la
base de confiance. Vérifier les mêmes empreintes dans la copie préparée avant
exécution, ainsi que les imports du compilateur inspectés par le coordinateur.

| Fichier | SHA-256 de la base |
| --- | --- |
| `build_front.py` | `54c70bccdfecd1e6ec8962cc211a6721cccd2d08b36a6517658a12de011e4481` |
| `test_v7.py` | `a1eaab580145e0bd1a90693d50a0e9200b9f80d2ce07213b6a32f3e14ccd65fa` |
| `tests/verify_course_native.cjs` | `87c5c6886bbc2d459ce8ccda8ad79a802a08768ae5b49555ddd3ead061128864` |
| `tests/verify_s01_browser.cjs` | `d859e435e9008503b8c1f19ec1764d6e81b47b3da6332b7f0880e31dcf303eb0` |
| `tests/browser_runtime.cjs` | `a344354e55267f6ace0f587fbd9076badede449731a792099d7e1be58c4adf94` |
| `tests/audit_fragments.py` | `bc06dd7d75894c668e69c18c8e5557c8b95f241dd1b49cf9799fe08bb4e1b3a4` |
| `tests/verify_categories.cjs` | `ee14fd397cd09dc44f4ec9a05577baa83de62212f328f8facc511d18b1bd7fc0` |

## Variables et sorties hors du dépôt

Les chemins suivants sont des emplacements proposés ; `I83_CONTROL_ROOT` doit
désigner la copie effectivement préparée et inspectée. Le répertoire de sortie
reste distinct de cette copie et du checkout canonique.

```bash
export I83_CONTROL_ROOT=/workspace/medina-env/i83-inspected
export I83_CONTROL_OUT=/workspace/medina-env/i83-0974d85-output
export I83_CONTROL_REPORTS=/workspace/medina-env/i83-0974d85-controls
export PYTHONDONTWRITEBYTECODE=1
export MEDINA_CHROMIUM=/usr/bin/chromium
export MEDINA_CHROMIUM_PATH=/usr/bin/chromium
mkdir -p "$I83_CONTROL_OUT" "$I83_CONTROL_REPORTS"
cd "$I83_CONTROL_ROOT"
```

Le `ROOT` de `test_v7.py`, des scripts Node et de `audit_fragments.py` dérive de
leur emplacement physique. Exécuter ces fichiers **depuis la copie**, même avec
un répertoire courant différent. `MEDINA_ROOT` est reconnu par `build_front.py`,
mais ne redirige pas le `ROOT` de ces tests.

## Construction et contrôles prioritaires

```bash
MEDINA_ROOT="$I83_CONTROL_ROOT" MEDINA_OUT="$I83_CONTROL_OUT" \
  python3 "$I83_CONTROL_ROOT/build_front.py" \
  > "$I83_CONTROL_REPORTS/build-global.log" 2>&1

MEDINA_ROOT="$I83_CONTROL_ROOT" MEDINA_OUT="$I83_CONTROL_OUT" \
  python3 "$I83_CONTROL_ROOT/build_front.py" --fragment S01 \
  > "$I83_CONTROL_REPORTS/build-s01.log" 2>&1

MEDINA_OUT="$I83_CONTROL_OUT" \
  python3 "$I83_CONTROL_ROOT/test_v7.py" --static I83 \
  > "$I83_CONTROL_REPORTS/static-i83.log" 2>&1

MEDINA_OUT="$I83_CONTROL_OUT" \
  python3 "$I83_CONTROL_ROOT/test_v7.py" I83 \
  > "$I83_CONTROL_REPORTS/global-browser-i83.log" 2>&1

MEDINA_NATIVE_CODE=I83 \
MEDINA_FRAGMENTS="$I83_CONTROL_OUT/fragments" \
MEDINA_QA_OUT="$I83_CONTROL_REPORTS/native-i83" \
  node "$I83_CONTROL_ROOT/tests/verify_course_native.cjs" \
  > "$I83_CONTROL_REPORTS/native-i83.log" 2>&1

MEDINA_CATEGORY_FRAGMENT_IDS=S01 \
MEDINA_FRAGMENTS="$I83_CONTROL_OUT/fragments" \
MEDINA_QA_OUT="$I83_CONTROL_REPORTS/categories-s01" \
  node "$I83_CONTROL_ROOT/tests/verify_categories.cjs" \
  > "$I83_CONTROL_REPORTS/categories-s01.log" 2>&1
```

Exécuter chaque commande séparément et consigner son code de sortie avant de
passer à la suivante. Une construction terminée avec un message
`non couvertes` dans le glossaire nécessite l'examen de ce résultat.

- `test_v7.py --static I83` vérifie les abréviations, références de fenêtres,
  préfixes, classes permises et styles en ligne des sources HTML.
- `test_v7.py I83` contrôle l'HTML **global** à 1300 × 900 puis 390 × 844 :
  cours, mots verts visibles sur ordinateur, quatre onglets, Navigo, taille de
  lecture, mode Livre, mode sombre lorsqu'il existe, débordement mobile et
  erreurs JavaScript. Il lit `$MEDINA_OUT/MEDINA.html`.
- `verify_course_native.cjs` découvre le fragment original d'I83 grâce aux
  données d'organisation compilées. Il vérifie, à **1360 × 900 et 390 × 844**,
  chaque déclencheur natif, les fenêtres sources et injectées, les chemins
  imbriqués, titres et textes complets attendus, Retour, Échap, focus, liens de
  sources et débordements. Le rapport distingue les modèles canoniques des
  dépendances partagées et vérifie la stabilité des entrées. Il produit
  `i83_native_results.json` ou `failed_i83_native_results.json`.
- `verify_categories.cjs` avec `MEDINA_CATEGORY_FRAGMENT_IDS=S01` vérifie le
  catalogue S01, ses catégories et cours avec des compteurs **dynamiques**, les
  noms du registre, contrastes et positions, quatre onglets et navigation.
  Il contrôle aussi l'accueil et les catégories à **390 × 844**, après le
  bureau à 1440 × 1000, et les outils de lecture/QCM d'I21. Ce contrôle de
  fragment complète le contrôle exhaustif des interactions propres à I83.
  Il produit `categories_results.json`.

Ces formats mobiles changent le viewport d'un contexte Chromium de bureau.
Ils ne constituent pas une émulation de Safari/iOS ou un test matériel tactile.

## Limite connue du contrôle S01 historique

La commande de ce script est :

```bash
MEDINA_S01_FILE="$I83_CONTROL_OUT/fragments/MEDINA_S01_cardiovasculaire.html" \
MEDINA_QA_OUT="$I83_CONTROL_REPORTS/s01-historical" \
  node "$I83_CONTROL_ROOT/tests/verify_s01_browser.cjs"
```

Le code de confiance contient l'assertion fixe `data.integrated === 20` et
`new Set(data.codes).size === 20`. L'ajout intégré d'I83 fait normalement passer
S01 à 21 cours : le script historique s'arrête alors à l'accueil. Consigner cet
échec comme incompatibilité du jeu de référence et ne pas annoncer une réussite
de toute sa suite. `verify_categories.cjs` et le contrôle natif I83 permettent
une validation indépendante avec les scripts existants, sans modifier cette
assertion. Le script historique sert déjà son HTML sur HTTP local, mais termine
par un contrôle distinct de portabilité `file://`.

## Adaptation HTTP lorsque file:// est bloqué

`test_v7.py`, `verify_course_native.cjs` et `verify_categories.cjs` ouvrent des URL
`file://` et n'offrent pas de variable URL. Les helpers existants
`/workspace/medina-env/check_browser.py` et `check_a41.py` ont des chemins et ports
fixes : ils ouvrent `/workspace/Medina/test_v7.py`, donc ne ciblent pas la copie
I83. Pour cette copie, employer les adaptations de transport suivantes hors du
checkout. Elles préservent toutes les assertions des scripts de confiance.
Consigner dans le rapport que le navigateur a utilisé HTTP local ; la portabilité
`file://` reste distincte et non établie si la machine la bloque.

### Python : test global avec serveur éphémère

Cette commande remplace uniquement `Page.goto` pour les HTML construits sous
`I83_CONTROL_OUT`, puis exécute le script de confiance situé dans la copie.

```bash
MEDINA_OUT="$I83_CONTROL_OUT" python3 - I83 \
  > "$I83_CONTROL_REPORTS/global-browser-i83-http.log" 2>&1 <<'PY'
import functools, http.server, os, runpy, sys, threading
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
from playwright.sync_api import Page

root = Path(os.environ['I83_CONTROL_ROOT']).resolve()
output = Path(os.environ['I83_CONTROL_OUT']).resolve()
class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass
handler = functools.partial(QuietHandler, directory=str(output))
server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
threading.Thread(target=server.serve_forever, daemon=True).start()
origin = 'http://127.0.0.1:' + str(server.server_port)
original_goto = Page.goto
def local_goto(self, value, *args, **kwargs):
    parsed = urlsplit(value)
    if parsed.scheme == 'file':
        relative = Path(unquote(parsed.path)).resolve().relative_to(output)
        value = origin + '/' + quote(relative.as_posix(), safe='/')
        if parsed.query:
            value += '?' + parsed.query
        if parsed.fragment:
            value += '#' + parsed.fragment
    return original_goto(self, value, *args, **kwargs)
Page.goto = local_goto
sys.argv = [str(root / 'test_v7.py'), 'I83']
try:
    runpy.run_path(str(root / 'test_v7.py'), run_name='__main__')
finally:
    server.shutdown()
    server.server_close()
PY
```

### Node : préchargeur de transport hors du checkout

Enregistrer ce helper, rédigé ici et à inspecter avant usage, sous
`$I83_CONTROL_REPORTS/http-preload.cjs`. Il n'a pas été exécuté dans la préparation
du protocole. Le serveur écoute exclusivement sur loopback avec un port
éphémère ; seul le répertoire de construction est servi. L'interception des
requêtes externes par les tests demeure active et laisse passer ce serveur local.

```javascript
const fs = require('node:fs'), http = require('node:http'), path = require('node:path');
const {fileURLToPath} = require('node:url');
const {chromium} = require('playwright');
const output = fs.realpathSync(process.env.I83_CONTROL_OUT);
let server, ready, origin;
function start() {
  if (!ready) ready = new Promise((resolve, reject) => {
    server = http.createServer((request, response) => {
      try {
        const relative = decodeURIComponent(new URL(request.url, 'http://local').pathname).slice(1);
        const file = fs.realpathSync(path.resolve(output, relative));
        const inside = path.relative(output, file);
        if (inside === '..' || inside.startsWith('..' + path.sep) || path.isAbsolute(inside)) {
          response.writeHead(403); response.end(); return;
        }
        response.setHeader('Content-Type', 'text/html; charset=utf-8');
        response.end(fs.readFileSync(file));
      } catch (error) { response.writeHead(404); response.end(); }
    });
    server.once('error', reject);
    server.listen(0, '127.0.0.1', () => {
      origin = 'http://127.0.0.1:' + server.address().port;
      resolve();
    });
  });
  return ready;
}
function wrapPage(page) {
  const goto = page.goto.bind(page);
  page.goto = async (value, options) => {
    const parsed = new URL(value);
    if (parsed.protocol === 'file:') {
      const file = fs.realpathSync(fileURLToPath(parsed));
      const relative = path.relative(output, file);
      if (relative === '..' || relative.startsWith('..' + path.sep) || path.isAbsolute(relative)) {
        throw new Error('HTML demandé hors du répertoire de construction');
      }
      await start();
      value = origin + '/' + relative.split(path.sep).map(encodeURIComponent).join('/') + parsed.search + parsed.hash;
    }
    return goto(value, options);
  };
  return page;
}
function wrapContext(context) {
  const route = context.route.bind(context);
  context.route = (pattern, handler, options) => route(pattern, async (requestRoute, ...args) => {
    if (origin && new URL(requestRoute.request().url()).origin === origin) return requestRoute.continue();
    return handler(requestRoute, ...args);
  }, options);
  const newPage = context.newPage.bind(context);
  context.newPage = async (...args) => wrapPage(await newPage(...args));
  return context;
}
const launch = chromium.launch.bind(chromium);
chromium.launch = async (...args) => {
  const browser = await launch(...args);
  const newContext = browser.newContext.bind(browser);
  browser.newContext = async (...values) => wrapContext(await newContext(...values));
  const newPage = browser.newPage.bind(browser);
  browser.newPage = async (...values) => wrapPage(await newPage(...values));
  const close = browser.close.bind(browser);
  browser.close = async (...values) => {
    try { return await close(...values); }
    finally { if (server) await new Promise(resolve => server.close(resolve)); }
  };
  return browser;
};
```

Commandes des scripts inchangés avec ce préchargeur :

```bash
MEDINA_NATIVE_CODE=I83 \
MEDINA_FRAGMENTS="$I83_CONTROL_OUT/fragments" \
MEDINA_QA_OUT="$I83_CONTROL_REPORTS/native-i83-http" \
  node -r "$I83_CONTROL_REPORTS/http-preload.cjs" \
  "$I83_CONTROL_ROOT/tests/verify_course_native.cjs" \
  > "$I83_CONTROL_REPORTS/native-i83-http.log" 2>&1

MEDINA_CATEGORY_FRAGMENT_IDS=S01 \
MEDINA_FRAGMENTS="$I83_CONTROL_OUT/fragments" \
MEDINA_QA_OUT="$I83_CONTROL_REPORTS/categories-s01-http" \
  node -r "$I83_CONTROL_REPORTS/http-preload.cjs" \
  "$I83_CONTROL_ROOT/tests/verify_categories.cjs" \
  > "$I83_CONTROL_REPORTS/categories-s01-http.log" 2>&1
```

## Audit complet et reproductibilité : périmètre facultatif

`tests/audit_fragments.py` exige **les 22 fragments** ; il n'accepte pas de filtre
S01. `MEDINA_FRAGMENTS` redirige les HTML examinés, mais ses fichiers temporaires
JavaScript et ses deux constructions de reproductibilité sont créés sous son
`ROOT`, dérivé du fichier du script. Son exécution convient uniquement à la copie
de contrôle, après construction de tous les fragments, avec cette particularité
explicitement enregistrée. Ce n'est pas le contrôle ciblé minimal d'I83.

```bash
MEDINA_ROOT="$I83_CONTROL_ROOT" MEDINA_OUT="$I83_CONTROL_OUT" \
  python3 "$I83_CONTROL_ROOT/build_front.py" --all-fragments

MEDINA_FRAGMENTS="$I83_CONTROL_OUT/fragments" \
  python3 "$I83_CONTROL_ROOT/tests/audit_fragments.py"
```

Pour vérifier la reproductibilité **globale** avec des sorties entièrement hors
de la copie, construire avec `MEDINA_OUT` dirigé successivement vers deux
répertoires externes, puis comparer les SHA-256 des `MEDINA.html`. Le code du
compilateur utilise `gzip(..., mtime=0)`. Une seule construction ne prouve pas la
reproductibilité ; les contrôles navigateur ne la prouvent pas non plus.

## Preuves à joindre à la décision

Consigner les SHA exacts de base/remise/copie candidate, la liste des fichiers
appliqués et leurs empreintes, celles des scripts de confiance, chaque commande
et code de sortie, les rapports JSON, dimensions des viewports et éventuelles
adaptations HTTP. Distinguer les échecs du contenu des limites du jeu de
référence, puis les résultats de la copie des vérifications après injection.
Les contrôles ci-dessus établissent le comportement technique et la conservation
des contenus examinés ; l'audit médical et l'audit croisé avant injection restent
des étapes distinctes.
