/* Shared browser discovery for MEDINA checks, without a machine-specific path. */
const fs = require('node:fs');
const path = require('node:path');

function loadPlaywright() {
  const candidates = ['playwright'];
  if (process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES) {
    candidates.push(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES, 'playwright'));
  }
  for (const candidate of candidates) {
    let resolved;
    try { resolved = require.resolve(candidate); }
    catch (error) { if (error.code === 'MODULE_NOT_FOUND') continue; throw error; }
    return require(resolved);
  }
  throw new Error('Playwright est absent. Installer : npm install --no-save playwright, puis npx playwright install chromium.');
}

function executable(file) {
  if (!file) return false;
  try {
    fs.accessSync(file, process.platform === 'win32' ? fs.constants.F_OK : fs.constants.X_OK);
    return fs.statSync(file).isFile();
  } catch { return false; }
}

function systemChromium() {
  const names = process.platform === 'win32'
    ? ['chromium.exe', 'chrome.exe']
    : ['chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable'];
  for (const directory of (process.env.PATH || '').split(path.delimiter).filter(Boolean)) {
    for (const name of names) {
      const file = path.join(directory, name);
      if (executable(file)) return file;
    }
  }
  const installed = process.platform === 'darwin'
    ? ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium']
    : process.platform === 'win32'
      ? [process.env.LOCALAPPDATA, process.env.PROGRAMFILES, process.env['PROGRAMFILES(X86)']]
          .filter(Boolean).map(root => path.join(root, 'Google', 'Chrome', 'Application', 'chrome.exe'))
      : [];
  return installed.find(executable);
}

function browserOptions(chromium) {
  let executablePath;
  if (process.env.MEDINA_CHROMIUM_PATH) {
    executablePath = path.resolve(process.env.MEDINA_CHROMIUM_PATH);
    if (!executable(executablePath)) {
      throw new Error('MEDINA_CHROMIUM_PATH ne désigne pas un navigateur exécutable : ' + executablePath);
    }
  } else if (!executable(chromium.executablePath())) {
    executablePath = systemChromium();
    if (!executablePath) {
      throw new Error('Chromium est absent. Installer le navigateur avec npx playwright install chromium, ou définir MEDINA_CHROMIUM_PATH vers un exécutable existant.');
    }
  }
  return {
    ...(executablePath ? {executablePath} : {}),
    ...(process.platform === 'linux' ? {args:['--no-sandbox', '--disable-dev-shm-usage', '--no-zygote', '--disable-gpu']} : {})
  };
}

module.exports = {loadPlaywright, browserOptions};
