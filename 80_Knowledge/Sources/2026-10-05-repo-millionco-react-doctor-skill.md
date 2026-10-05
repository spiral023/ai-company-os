---
url: https://github.com/millionco/react-doctor/tree/main/skills/react-doctor
autor: millionco
datum: 2026-10-05
erfasst: 2026-10-05
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# React Doctor: Health-Score für React-Code als Regressionsprüfung nach jeder Änderung

Im Klon von millionco/react-doctor (Stand Commit `1b149bae`) liegt der Agent-Skill `skills/react-doctor/SKILL.md` (Version 1.2.0). Gelesen, nichts ausgeführt.

## Kernaussagen
- React Doctor scannt React-Code auf Sicherheits-, Performance-, Korrektheits- und Architekturprobleme und gibt einen Health-Score von 0 bis 100 aus.
- Nach jeder Änderung soll der Agent `npx react-doctor@latest --verbose --scope changed` ausführen und vor dem Commit Regressionen beheben, wenn der Score sinkt.
- Weitere Modi: Vollscan für Aufräumarbeiten, `design` für ein UI-Audit, `scan <url>` zeichnet einen DevTools-Trace für Laufzeitprobleme auf.
- `/doctor` lädt ein zentral gepflegtes Triage-Playbook von react.doctor nach und arbeitet es ab (scannen, filtern, priorisieren, beheben, prüfen); es committet nie selbst.

## Einordnung
Ein Doctor-Werkzeug im engeren Sinn: Es prüft den aktuellen Zustand des Codes gegen feste Regeln, nicht den Verlauf einer Session. Das nachgeladene Playbook ändert sich ohne Skill-Update, das ist bequem, aber auch eine externe Abhängigkeit zur Laufzeit.

## Verbindungen
- [[Testharness-als-staerkster-Hebel]]
- [[Hook-Entscheidungstyp-nach-Pruefbarkeit]]
