# CI-Agent-mit-Review-Gate

**Konfidenz:** meinung

## Zweck

Ermöglicht, einen Coding Agent event-getriggert und automatisiert in CI/CD zu betreiben, ohne dass dafür ein eigener Freigabemechanismus erfunden werden muss. Adressiert das Risiko, dass automatisierte Agent-Läufe unbeaufsichtigt Änderungen in den Hauptbranch durchreichen.

## Funktionsweise

Der Agent läuft als eigener, sandboxed Job in der CI-Pipeline (z. B. GitLab CI, äquivalent auf GitHub Actions übertragbar), ausgelöst durch ein Event wie einen `@claude`-Kommentar in einem Issue oder einer Merge/Pull Request. Er arbeitet isoliert im Runner und spielt sein Ergebnis ausschließlich als Merge/Pull Request zurück — nie direkt in den Hauptbranch. Der Reviewer-Schritt wird dadurch nicht neu erfunden, sondern ist identisch mit dem ohnehin bestehenden Team-Review-Prozess für menschliche Beiträge. Für die Authentifizierung wird Provider-Abstraktion genutzt: dieselbe Job-Definition kann gegen die Modell-API direkt, gegen AWS Bedrock via OIDC-Token-Exchange oder gegen Google Vertex AI via Workload Identity Federation laufen, ohne dauerhaft gespeicherte statische Keys im Repository.

## Vorteile

- Kein separater Freigabemechanismus nötig — das bestehende Review-Gate des Teams (MR/PR) trägt automatisch auch die Agent-Änderungen.
- Sandboxed Execution begrenzt den Blast Radius eines fehlerhaften oder missbräuchlich getriggerten Laufs auf den isolierten Runner.
- Provider-Abstraktion über OIDC/Workload Identity Federation vermeidet statische, potenziell leckende API-Keys im Repository.
- Übertragbar über die konkrete CI-Plattform hinaus — das Muster (Event-Trigger → Sandbox → bestehendes Review-Gate) ist plattformunabhängig.

## Nachteile & Grenzen

- Das Review-Gate ist nur so wirksam wie der bestehende Team-Prozess dahinter — ein oberflächliches Review lässt fehlerhafte Agent-Änderungen genauso durch wie fehlerhafte menschliche.
- `CLAUDE.md`/`AGENTS.md` wird auch im CI-Job vollständig geladen — dieselbe Kürze-Disziplin wie bei lokaler Nutzung ist nötig, sonst steigen Kosten und Fehleranfälligkeit.
- Runner-Minuten und API-Token-Kosten laufen bei jedem Trigger, unabhängig vom Nutzen des Ergebnisses.
- Konkrete Konfigurationsdetails (Image-Tags, Install-Skripte, CLI-Flags) sind plattform- und zeitgebunden und verändern sich unabhängig vom Grundmuster.

## Wann einsetzen, wann nicht

- Einsetzen: Teams mit etabliertem MR/PR-Review-Prozess, die wiederkehrende Aufgaben (Issue-zu-MR, Bugfix aus Fehlerbeschreibung, Implementierungshilfe in laufender Diskussion) automatisieren wollen.
- Nicht einsetzen: Teams ohne belastbaren Review-Prozess — dort automatisiert das Muster nur die Zuführung ungeprüfter Änderungen; Aufgaben, die einen direkten Zugriff auf den Hauptbranch ohne Review erfordern, passen ebenfalls nicht.

## Belege

- 2026-02-01 · [[2026-02-01-anthropic-docs-claude-code-gitlab-ci]] · meinung — Offizielle Anthropic-Doku zu Claude Code in GitLab CI/CD beschreibt Event-Trigger, Sandboxed Execution und Provider-Abstraktion (Claude API/Bedrock/Vertex); Output läuft ausschließlich über den MR-Prozess.

## Spannungen & offene Fragen

- Einzige bisherige Quelle ist offizielle Herstellerdokumentation zu einer spezifischen CI-Plattform (GitLab) — noch nicht unabhängig für andere Plattformen (GitHub Actions, Jenkins) oder durch einen echten Betriebsbericht bestätigt.
- Offene Frage: Wie unterscheidet sich die Risikoabschätzung, wenn der CI-Agent nicht nur Code-Änderungen vorschlägt, sondern auch Tests oder Deploy-Schritte selbst auslösen darf?

## Verwandte Patterns

- [[Lokale-Modell-Umleitung-Muster]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Plan-first-mit-getrenntem-Review]]
