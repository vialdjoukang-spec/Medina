#!/usr/bin/env bash
# Reconstruit la publication du Cycle 2 sur main en 3 avances rapides validées par la garde.
# Usage : bash tools/claude_chaine_main.sh   (puis pousser C1, C2, C3 un par un vers main)
set -e
git fetch -q origin main
SB=$(git rev-parse origin/main:.claude/settings.json 2>/dev/null || true)
mk(){ export GIT_INDEX_FILE=$(mktemp); git read-tree "$1"; git ls-tree -r HEAD tools tests build_front.py | git update-index --index-info
  [ -n "$SB" ] && git update-index --add --cacheinfo 100644,$SB,.claude/settings.json
  T=$(git write-tree); rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE; git commit-tree $T -p "$2" -m "$3"; }
S1=$(git log --format=%H --grep="transfert enregistré de Codex" -1)
S2=$(git log --format=%H --grep="passage unique en publication directe ; plancher" -1)
C1=$(mk $S1 origin/main "Cycle 1 audité, outils, garde des cycles Claude et transfert du Cycle 2 à Claude")
C2=$(mk $S2 $C1 "Cycle 2 : passage unique en publication directe")
C3=$(mk HEAD $C2 "Cycle 2 : contrôles coordinateur, quatre leçons prêtes à injecter ; état courant")
for p in "origin/main $C1" "$C1 $C2" "$C2 $C3"; do python3 tools/espace.py garde $p | tail -1; done
echo "C1=$C1 C2=$C2 C3=$C3"
echo "Ensuite : git push origin \$C1:main ; git push origin \$C2:main ; git push origin \$C3:main"
