# Hook-Entscheidungstyp-nach-Pruefbarkeit

**Konfidenz:** meinung

## Zweck

Hilft, die richtige Implementierungsart für eine Hook-Entscheidung zu wählen, statt reflexhaft immer zum starren Shell-Skript oder immer zum freien Modellurteil zu greifen. Adressiert, dass nicht jede Hook-Bedingung gleich gut vorab in Code formulierbar ist.

## Funktionsweise

Drei Entscheidungsformen stehen zwischen starrem Skript und freiem, unstrukturiertem Modellurteil, abgestuft nach Prüfbarkeit der zugrunde liegenden Bedingung: **Deterministisches Shell-Skript** für Bedingungen, die sich vollständig vorab in Code formulieren lassen (z. B. „enthält der Pfad `.env`?“) — schnell, aber nur für vorher bekannte, klar formulierbare Fälle geeignet. **Prompt-based Hook** (`type: "prompt"`), bei dem ein LLM die Ja/Nein-Entscheidung trifft, statt dass ein Skript sie per Pattern-Matching berechnet — für Bedingungen, die sprachliches Urteil statt reiner Musterprüfung brauchen. **Agent-based Hook** (`type: "agent"`), bei dem ein Subagent mit eigenem Tool-Zugriff eine Bedingung prüft, die sich nicht ohne tatsächliche Ausführung feststellen lässt (Beispiel: „Laufen alle Tests?“) — die flexibelste, aber auch am wenigsten vorhersagbare Stufe. Die Wahl folgt der Prüfbarkeit der Bedingung selbst: klar codierbar → Skript, sprachliches Urteil nötig → Prompt-Hook, Ausführung/Tool-Zugriff nötig → Agent-Hook.

## Vorteile

- Macht die Wahl der Hook-Implementierung explizit von der Prüfbarkeit der Bedingung abhängig, statt sie dem Zufall der gerade bekannten Technik zu überlassen.
- Deckt einen Bedingungstyp ab (Ausführung nötig, z. B. Testlauf), den ein reines Skript strukturell nicht prüfen kann, ohne gleich auf unstrukturiertes Modellurteil auszuweichen.
- Erweitert das Hook-Konzept über reine Deterministik hinaus, ohne die Vorhersagbarkeit dort aufzugeben, wo sie tatsächlich möglich ist.

## Nachteile & Grenzen

- Nur als knappe Zwei-Punkt-Erwähnung ohne Vertiefung belegt — keine Beispiele, keine Kostenangabe, keine Aussage zur tatsächlichen Zuverlässigkeit von Prompt- oder Agent-Hooks im Vergleich zum Skript-Hook.
- Prompt- und Agent-Hooks geben einen Teil der Vorhersagbarkeit auf, die den deterministischen Shell-Hook überhaupt erst attraktiv macht — die Abstufung ist ein Trade-off, keine reine Verbesserung.
- Agent-Hooks sind die teuerste und langsamste Stufe (voller Subagent-Lauf für eine einzelne Bedingung) — unverhältnismäßig für Bedingungen, die sich doch noch in ein Skript fassen lassen.

## Wann einsetzen, wann nicht

- Einsetzen: beim Entwurf einer neuen Hook-Bedingung, wenn unklar ist, ob ein Skript ausreicht oder sprachliches Urteil bzw. tatsächliche Ausführung nötig ist.
- Nicht einsetzen: wenn die Bedingung bereits klar deterministisch codierbar ist — dort ist das einfache Skript ohne Umweg über diese Abwägung die richtige Wahl.

## Belege

- 2026-02-01 · [[2026-02-01-anthropic-docs-automate-workflows-with-hooks]] · meinung — Anthropics eigene Hooks-Dokumentation nennt neben dem klassischen deterministischen Shell-Hook zwei weitere Hook-Typen (`type: "prompt"`, `type: "agent"`) mit dem Agent-Hook-Beispiel „Laufen alle Tests?“, führt die Unterscheidung aber selbst nicht weiter aus.
- 2026-09-18 · [[2026-09-18-akshay_pachaar-2101037514945597645]] · meinung — Empfiehlt semantisches Risiko-Gating vor Tool-Calls (read-only, reversibel, destruktiv) nur als Ergänzung zu deterministischen Kontrollen wie Permissions, Sandbox und Tests. Einschränkung: Modell ist Closed Weights und nur im Early Access.
- 2026-09-27 · [[2026-09-27-anthropic-academy-sdlc-playbook]] · meinung — Hooks als deterministische Ebene hinter beratenden Skills: schnelle dateibezogene Build-Hooks, Testdatei-Sperre bei Bugfixes, Deploy-Gate per Exit-Code 2, nicht verhandelbare Hooks in verwalteten Einstellungen. Nur Konzept und Beispiele, keine Auswertung.
- 2026-09-04 · [[2026-09-04-julian-ivanov-ki-automat-so-nutzt-du-claude-code-nach-anthropics-neuen-re]] · meinung — Stützt die Trennung: CLAUDE.md ist nur Kontext und wird bei vollem Context Window auch ignoriert, garantierte Aktionen (Umlaute prüfen, Credential-Dateien sperren) gehören in Hooks. Anfängerorientierte Aufbereitung, keine eigene Messung.
- 2026-08-21 · [[2026-08-21-openknowledge-open-knowledge-format-plugin-for-llm-wikis-openk]] · meinung — Lint-Ergebnisse werden als Warnung an die MCP-Tool-Antwort gehängt, blockieren den Write nicht und kosten keinen Extra-Call; harte Durchsetzung läuft getrennt über `ok lint` in CI. Herstellerangabe ohne Messung, ob Agents die Warnungen befolgen.
- 2026-08-05 · [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]] · meinung — Rules sind keine Garantie, weil sie in langen Sessions untergehen; ergänzend statische Code-Analyse per Script als deterministische Prüfung. Erfahrungsbericht.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, dort nur in zwei Sätzen ohne Vertiefung erwähnt — eine zweite, unabhängige Quelle würde die Aussage deutlich stärken, bevor sie über den Status einer Einzelbeobachtung hinauswächst.
- Offene Frage: Wie verhält sich die Zuverlässigkeit eines Prompt-Hooks gegenüber einem Skript-Hook in der Praxis — gibt es Bedingungen, bei denen der Prompt-Hook trotz sprachlicher Flexibilität systematisch unzuverlässiger entscheidet?

## Verwandte Patterns

- [[Hook-erzwungene-Skill-Aktivierung]]
- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
