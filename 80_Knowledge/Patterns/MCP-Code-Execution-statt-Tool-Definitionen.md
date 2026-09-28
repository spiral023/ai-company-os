# MCP-Code-Execution-statt-Tool-Definitionen

**Konfidenz:** meinung

## Zweck

Löst das in [[Erweiterungs-Ebenen-Zuordnung]] bereits benannte Kostenproblem von MCP-Servern an der Wurzel: Viele konfigurierte MCP-Tools blähen den Kontext mit ihren Schemas auf, bevor überhaupt ein einziges Tool genutzt wird — unabhängig davon, wie viele davon eine Aufgabe tatsächlich braucht.

## Funktionsweise

Statt jedes MCP-Tool als dauerhaft geladene Definition in den Kontext zu legen, bekommt das Modell eine Sandbox und schreibt selbst Code, der die MCP-Tools zur Laufzeit aufruft — die Tool-Schemas müssen dafür nicht permanent im Kontext stehen, sondern werden erst beim tatsächlichen Aufruf relevant. Das verschiebt MCP von „viele Tool-Definitionen vorab in den Kontext laden“ zu „ein Ausführungsraum, den das Modell bei Bedarf programmatisch nutzt“ — dieselbe Progressive-Disclosure-Logik, die Skills schon auf Instruktionsebene anwenden, hier auf Tool-Schemas übertragen.

## Vorteile

- Entkoppelt die Zahl konfigurierter MCP-Server von den permanenten Kontextkosten — mehr verfügbare Tools kosten nicht mehr automatisch mehr Kontext pro Turn.
- Passt dieselbe Progressive-Disclosure-Idee, die bei Skills schon etabliert ist, auf eine Kategorie an, die bisher primär über Reduktion der aktiven Serverzahl adressiert wurde (siehe [[Erweiterungs-Ebenen-Zuordnung]]).
- Reduziert das in [[Erweiterungs-Ebenen-Zuordnung]] dokumentierte Problem, dass „viele MCPs konfigurieren, aber nur wenige aktiv halten“ ein manuelles Kuratieren erfordert.

## Nachteile & Grenzen

- Erfordert eine Sandbox-Ausführungsumgebung für vom Modell selbst geschriebenen Code — mehr Infrastruktur als reines Tool-Calling.
- Nur knapp erwähnt in der bisherigen Quelle, ohne technische Details zu Fehlerbehandlung, Sicherheitsgrenzen der Sandbox oder tatsächlicher Kontextersparnis in Zahlen.
- Modellgenerierter Aufruf-Code kann eigene Fehlerquellen einführen (falsche API-Nutzung, Halluzination von Parametern), die bei direktem Tool-Calling mit festem Schema seltener auftreten.

## Wann einsetzen, wann nicht

- Einsetzen: bei vielen konfigurierten MCP-Servern, deren Tool-Schemas den Kontext spürbar belasten, und wenn eine Sandbox-Infrastruktur bereits vorhanden oder vertretbar ist.
- Nicht einsetzen: bei wenigen, immer relevanten MCP-Tools ohne spürbares Kontextproblem — dort ist direktes Tool-Calling einfacher und weniger fehleranfällig.

## Belege

- 2026-01-25 · [[2026-01-25-sankalp-claude-code-experience]] · meinung — Nennt „MCP Code Exec“ knapp als Lösung für die MCP-Kontextfalle: Sandbox statt vieler Tool-Definitionen, Modell schreibt selbst Aufruf-Code.
- 2026-09-17 · [[2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access]] · meinung — Beschreibt ein Code-Mode-Gateway (ein Skript-Tool vor vielen MCP-Servern, Suche, dann Skript mit Ausgabefilter) und nennt `executor` sowie ein Docker-Gateway als Umsetzungen. Rein behauptet, ohne Messwerte; Autor bewirbt einen eigenen Kurs.
- 2026-02-01 · [[2026-02-01-anthropic-docs-connect-claude-code-to-mcp]] · meinung — Tool Search lädt MCP-Definitionen dynamisch ab 10 % Context-Window-Anteil; Gegenmaßnahme gegen Definitions-Overhead, aber kein Code-Execution-Ansatz.
- 2026-01-15 · [[2026-01-15-avasdr34m-its-not-easy-but-it-is-simple-kontext-nutzung-in-claude-code-entscheidet]] · meinung — Tool-Beschreibungen vieler MCP-Server belegen dauerhaft Context (Faustwert etwa 500 Token je Tool); nur Faustzahl.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, sehr knapp beschrieben — keine unabhängige Zweitbestätigung, keine Zahlen zur tatsächlichen Kontextersparnis oder zu Fehlerraten gegenüber klassischem Tool-Calling.

## Verwandte Patterns

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[Klein-und-komposierbar]]
