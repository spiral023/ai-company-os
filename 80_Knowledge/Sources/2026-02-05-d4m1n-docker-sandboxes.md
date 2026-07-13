---
url: https://x.com/d4m1n/status/2019366063226355930
autor: "Dan (@d4m1n)"
datum: 2026-02-05
erfasst: 2026-07-13
typ: tweet
---

# Dan (@d4m1n) zu „AI Agents sicher im YOLO-Modus mit Docker Sandboxes“

## Inhalt

YOLO-Modus (Auto-Approval/Skip-Permissions) macht Agenten schneller und ermöglicht lange autonome Läufe (z.B. Ralph Loop über Nacht), erhöht aber das Risiko unbeabsichtigter destruktiver Befehle auf dem Hauptsystem. Docker „Sandboxes“ (neues Feature) isoliert Agent-CLIs mit einem Einzeiler: `docker sandbox run claude .` (analog `codex .`, `gemini .`) — erstellt im Hintergrund eine leichtgewichtige Micro-VM mit eigenem, privaten Docker-Daemon; das Host-System bleibt unangetastet. Einmaliger Login in den jeweiligen Account nötig. Für einen Ralph Loop in der Sandbox reicht ein einfaches Bash-Script, das `docker sandbox run claude . -- -p "$PROMPT_CONTENT"` in einer Schleife über `MAX_ITERATIONS` ausführt. Debugging/Inspektion: `docker sandbox list` zeigt aktive Sandboxes, `docker sandbox exec -it <name> bash` klinkt sich direkt in eine laufende Sandbox ein (volle Kontrolle wie bei einem regulären Container, aber mit Micro-VM-Isolation).

## Kernaussagen

- Docker Sandboxes (`docker sandbox run <agent> .`) isolieren Agent-CLIs mit einem Einzeiler in einer Micro-VM mit eigenem Docker-Daemon — Voraussetzung, um YOLO-Modus/Ralph-Loop-Läufe sicher über Nacht laufen zu lassen, ohne das Host-System zu gefährden → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
- Trotz Isolation bleibt volle Debug-Kontrolle erhalten (`docker sandbox list`/`exec`) — Sicherheit und Inspizierbarkeit schließen sich nicht aus → [[Ralph-Loop-Frischer-Kontext-pro-Iteration]]
