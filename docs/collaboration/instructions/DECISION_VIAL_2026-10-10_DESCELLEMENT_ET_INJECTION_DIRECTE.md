# Décision de Vial Djoukang (propriétaire de MEDINA) — descellement total et injection directe

Dates : 9 et 10 octobre 2026 (Europe/Zurich), dans la conversation du propriétaire avec Grok Bot.

## 1. Injection directe dans main sans attente d'audit (9 octobre 2026, 22 h 40)

Vial a décidé que le prompt de continuité est injecté directement et que le travail
des auteurs reste accessible dans main, l'espace final de MEDINA, même s'il n'est
pas encore audité, pour que le travail ne soit pas perdu si la limite d'utilisation
s'épuise. Formulation transmise : « pas d'attente d'audit pour rendre le travail
accessible. L'audit se fera plus tard. »

## 2. Descellement de tous les cours (10 octobre 2026, 00 h 04)

Vial a choisi « Descelle les 26 leçons de cardiologie et applique-leur le contrôle
complet », puis a écrit « Desceller TOUT ». Le scellement s'arrête donc pour toutes
les spécialités : `organisation/SCELLES.json` porte `"scelle": false`.

## Portée

Cette décision couvre les livraisons des quatre auteurs de spécialité :
cardiologie (S01), pneumologie (S02), gastro-entérologie et hépatologie (S03)
et infectiologie (T1). Elle s'applique par le registre d'injection directe prévu par
la section 12 de `docs/collaboration/LEADERSHIP_CLAUDE_2026-10-08.md` :
`organisation/SCELLES.json` enregistre l'empreinte de chaque source médicale
injectée. Ce registre atteste une décision d'injection, pas une validation médicale.
L'audit se fera plus tard.

## Procédure pour chaque livraison

Avant chaque commit qui modifie `chapters/`, `glossary/` ou `chapters.json`,
l'auteur lance `python3 tools/sceller.py enregistrer` et joint
`organisation/SCELLES.json` au même commit. La garde `tools/espace.py garde`
reste inchangée : elle refuse toujours une source médicale dont l'empreinte n'est
pas enregistrée, et les fragments INJECTE restent verrouillés.
