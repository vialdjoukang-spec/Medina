#!/bin/bash
# Applique la justification d'un cours, la contrôle sur une copie temporaire des sources canoniques,
# restaure ces sources et met à jour le manifeste. Usage : finaliser.sh <CODE>
set -e
CODE="$1"
cd "$(dirname "$0")/../../../../.."
J="livraisons/Livraison Claude/C-01-Cardiologie/travail/justification"
L="livraisons/Livraison Claude/C-01-Cardiologie/sources/chapters/$CODE"
python3 "$J/appliquer_justifications.py" "$CODE" "$J/$CODE" --ecrire
cp "$L"/*.html "chapters/$CODE/"
python3 test_v7.py --static "$CODE" || { git checkout -q -- "chapters/$CODE"; exit 1; }
git checkout -q -- "chapters/$CODE"
python3 "$J/manifeste.py" "$CODE"
python3 tools/livraison.py check-claude "livraisons/Livraison Claude/C-01-Cardiologie" | tail -1
