---
url: https://aseemshrey.in/blog/claude-codex-iterative-plan-review/
autor: "Aseem Shrey"
datum: 2026-02-20
erfasst: 2026-07-13
typ: artikel
---

# Aseem Shrey zu „Claude vs. Codex: Iterative Plan-Reviews für fehlerfreien Code“

## Inhalt

Problem „Single-Model Blindness“: Wenn Planung und Ausführung dieselbe Modellinstanz sind, argumentiert das Modell nicht mit sich selbst — es findet nicht von sich aus „dieses Auth-Modell ist unvollständig“. Beobachtete wiederkehrende Fehlermuster bei Single-Model-Planung: Pläne ohne klares Auth-Modell, Shell-Scripts mit Quoting-Fehlern, Schema-Designs mit widersprüchlichen Zustandsfeldern, fehlendes Concurrency-Handling in Multi-Agent-Szenarien.

Lösung: ein Claude-Code-Skill (`/codex-review`), der eine iterative Review-Schleife zwischen Claude (Planer) und OpenAI Codex CLI (Reviewer, read-only Sandbox) auslöst. Ablauf: Claude schreibt Plan in temporäre Datei → sendet an Codex → Codex antwortet mit `VERDICT: REVISE` oder `VERDICT: APPROVED` (max. 5 Runden) → bei REVISE überarbeitet Claude und die Codex-Session wird fortgesetzt (`codex exec resume <session-id>`, Kontext/Erinnerung an vorherige Aussagen bleibt erhalten) → Prüfung wiederholt sich gezielt auf die behobenen Punkte.

Konkretes Beispiel („Mission Control“-Dashboard für Multi-Agenten-Swarm): Vorher (Single-Pass) fehlte Auth für Agent-Endpoints, Shell-Scripts waren kaputt (`"$1"` in Single Quotes), Schema hatte redundante auseinanderlaufende Felder (`status`/`column`), kein Concurrency-Handling beim Task-Claiming. Nachher (3 automatisierte Runden, 14 gefundene und behobene Probleme): API-Key-Auth pro Agent, typisiertes CLI statt fragiler Shell-Scripts, atomare Lease-Claims mit optimistischer Parallelitätssteuerung, explizite ACL-Matrix, Integration-/Security-Tests.

Design-Begründungen: als Skill (on-demand), nicht als Hook — nicht jeder Plan braucht eine zweite Meinung, nur wo viel auf dem Spiel steht. Iterativ statt One-shot, weil ein One-shot-Review Probleme findet, aber die Korrektur nicht verifiziert (verhindert, dass „eine Sache repariert und zwei andere kaputt gemacht“ werden). VERDICT-Protokoll als klares Stopp-Signal, mit Rundenlimit als Sicherheitsnetz.

## Kernaussagen

- Cross-Model-Review (Codex prüft read-only Claudes Pläne) mit iterativer Session-Fortsetzung und explizitem VERDICT-Protokoll (APPROVED/REVISE, Rundenlimit) macht „Single-Model Blindness“ konkret behebbar → [[Plan-first-mit-getrenntem-Review]]
- Ein konkretes Vorher-Nachher-Beispiel belegt den Effekt: 3 automatisierte Runden fanden und behoben 14 Probleme (fehlende Auth, Shell-Quoting-Fehler, widersprüchliche Schema-Felder, fehlendes Concurrency-Handling) → [[Plan-first-mit-getrenntem-Review]]
- Review als on-demand Skill statt verpflichtendem Hook: nur bei hoher Tragweite aktivieren, nicht bei jeder kleinen Änderung → [[Plan-first-mit-getrenntem-Review]]
