#!/usr/bin/env python3
"""Hook Stop : refuse de clore une réponse au propriétaire sans la jauge verte 🟩 (une relance au plus)."""
import json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-Medina/32d77524-f01f-5b7e-92b4-188dd9e32b87/scratchpad/jauge')
from jauge import line
try:
    data = json.load(sys.stdin)
except Exception:
    data = {}
if data.get('stop_hook_active'):
    sys.exit(0)
text = data.get('last_assistant_message') or ''
if not text and data.get('transcript_path'):
    try:
        for raw in reversed(open(data['transcript_path'], encoding='utf-8').read().splitlines()):
            ev = json.loads(raw)
            msg = ev.get('message') or {}
            if ev.get('type') == 'assistant' and msg.get('role') == 'assistant':
                parts = [c.get('text', '') for c in msg.get('content', []) if isinstance(c, dict) and c.get('type') == 'text']
                if any(parts):
                    text = '\n'.join(parts); break
    except Exception:
        pass
if '🟩' in text or '⬜' in text:
    sys.exit(0)
print(json.dumps({'decision': 'block', 'reason': 'Termine ta réponse par la jauge verte, recopiée exactement : ' + line()}, ensure_ascii=False))
