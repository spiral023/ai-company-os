# CI-Agent-mit-Review-Gate

**Konfidenz:** mehrfach-belegt

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
- 2026-01-22 · [[2026-01-22-hooeem-claude-code-7-schritte-plan]] · meinung — Ergänzt drei konkrete Anthropic-Werkzeuge für dieselbe Grundidee: die GitHub-App prüft Pull Requests automatisch auf Bugs/Sicherheitsrisiken, Custom Instructions in `.github/workflows` tragen Team-Standards in CI, und das Claude Code SDK bettet dieselbe Intelligenz in eigene CI/CD-Pipelines ein.
- 2026-02-01 · [[2026-02-01-aiedge-claude-code-starter-pack]] · meinung — Boris Chernys Team installiert eine GitHub Action, die auf `@claude`-Tags in Pull-Request-Kommentaren reagiert, ausdrücklich als „unsere Version von @danshipper's Compounding Engineering“ bezeichnet — derselbe Event-Trigger-→-bestehendes-Review-Gate-Mechanismus wie die bisherige GitLab-CI-Quelle, hier für GitHub Actions und als echter Betriebsbericht statt nur Herstellerdoku bestätigt. Konfidenz entsprechend auf `mehrfach-belegt` angehoben.
- 2026-09-27 · [[2026-09-27-anthropic-academy-sdlc-playbook]] · meinung — Der schreibende Agent darf nicht selbst genehmigen, Agenten-Befunde blockieren keinen PR, Branch-Schutz mit Code-Owner-Freigabe bleibt; CI-Schreibschritte nur als PR, Autonomie nach Umgebung gestaffelt. Beschreibung ohne Wirkungszahlen.
- 2026-02-23 · [[2026-02-23-elvis-openclaw-codex-agent-swarm]] · meinung — Definition of Done aus grüner CI, Sync mit main, Screenshot bei UI-Änderung und drei AI-Reviewern vor dem menschlichen Review (5–10 Minuten laut Quelle). Neu ist die Modell-Rollenteilung der Reviewer; die Wirksamkeit ist nicht gemessen.
- 2026-08-14 · [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]] · meinung — Prüfmodell mindestens gleich stark wie Erzeuger, Merge nur mit Required Status Checks (Rulesets); Warnsignal, wenn der Agent Tests anpasst.
- 2026-02-20 · [[2026-02-20-boris-tane-sdlc-is-dead]] · meinung — Fordert Adversarial Agent statt menschlichem PR-Review; steht im Gegensatz zum Review-Gate, ungeprüft.
- 2026-09-29 · [[2026-09-29-openclaw-openclaw-enterprise-the-open-agent-platform-open]] · meinung — Interner Agent Androidclaw triagiert Kanäle, findet PRs und mergt Fixes; LLM-basierte Reviews als Teil der Plattform. Eigenbericht, ohne Zahlen.

## Spannungen & offene Fragen

- Die GitHub-Actions-Bestätigung (aiedge/Boris Cherny) und die drei hooeem-Werkzeuge bleiben Sekundärquellen ohne eigene Messung; die GitLab-Quelle bleibt die einzige Herstellerdokumentation. Trotzdem: drei organisatorisch unterschiedliche Quellen über zwei Plattformen stützen dasselbe Grundmuster jetzt über eine reine Einzelquelle hinaus.
- Offene Frage: Wie unterscheidet sich die Risikoabschätzung, wenn der CI-Agent nicht nur Code-Änderungen vorschlägt, sondern auch Tests oder Deploy-Schritte selbst auslösen darf?
- Spannung (2026-09-29): [[2026-02-20-boris-tane-sdlc-is-dead]] vertritt die These, ein Adversarial Agent könne den menschlichen Review ersetzen. Das widerspricht dem Kern dieses Patterns, den Agent-Output ausschließlich über das bestehende Team-Review-Gate laufen zu lassen. Belegt ist die These nur als Meinung (vibedeck-Sekundärquelle, keine Messung). Beide Positionen bleiben nebeneinander stehen.

## Verwandte Patterns

- [[Lokale-Modell-Umleitung-Muster]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[Plan-first-mit-getrenntem-Review]]
