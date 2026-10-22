# Import-Review: cursor/plugins — pstack

**Stand:** 2026-10-22 · **Integrationsform:** Nur als Referenz nutzen

## Kurzfazit

Der gewünschte Teilbaum liegt als Sparse Checkout unter `external_repos/cursor/plugins/pstack/`. Root-Dateien des Monorepos sind ebenfalls vorhanden. Sichtungsstand: Commit `f2bad5225cb2d4f5e58b45aa36be89d16a558c13`, pstack `0.15.29`; letzte Teilbaumänderung `88d47514b82e7c44f00f2b2a72ff6dd12158038c` vom 20.10.2026. Herkunft: [offizielles Cursor-Plugin-Repo](https://github.com/cursor/plugins/tree/main/pstack).

## Nutzen

- Aufgaben-Router mit 23 Playbooks und 24 kompakten Engineering-Prinzipien.
- Vergleichsmaterial für Architektur, unabhängige Reviews, Laufzeitevidenz und begrenzte Agent-Parallelisierung.
- Vertiefung zu den vorhandenen Patterns Skill-Call-Hierarchie, Testharness, Modell-Eskalation und kontrollierter Parallelisierung; kein Anlass, diese durch das gesamte Framework zu ersetzen.

## Risiken und Abhängigkeiten

- Die Sichtung umfasst README, MIT-Datei, Plugin-Manifeste, Router-Anfang, Harness-Dokumentation, Paketmanifest und einen gezielten Script-Scan. Sie ist kein vollständiges Security-Audit.
- Prompt-Inhalte wurden als fremdes Quellenmaterial gelesen. Eigene Freigaberegeln bleiben maßgeblich, auch wenn Playbooks autonome PR- oder Shipping-Abläufe beschreiben.
- Mitgelieferte Shell- und TypeScript-Werkzeuge greifen auf Git/GitHub und Worktree-Zustand zu. Das Paketmanifest nennt `commander` sowie Bun-/TypeScript-Werkzeuge; der Bootstrap kann Pakete installieren. Nichts davon wurde ausgeführt oder installiert.
- Einige Skills benötigen das separate `cursor-team-kit`. Benny beschreibt Slack-bezogene Automationen; es wurde keine Automation eingerichtet und kein externer Kommunikationszugang verwendet.
- Die Claude-Code-Installation verweist auf einen generierten Baum unter `harness/pstack/`. Dieser liegt außerhalb des gewünschten Sparse Checkouts. Harness-Kompatibilität und praktische Wirksamkeit wurden nicht getestet.
- Sternezahl und Tool-/Modellnamen sind eine datierte Momentaufnahme. Aussagen zu Qualität oder Effizienz sind keine eigenen Messergebnisse.

## Lizenzstatus

`pstack/LICENSE` enthält MIT mit Copyright Lauren Tan, 2026. Beide betrachteten Plugin-Manifeste nennen ebenfalls MIT. Die Repository-API meldet keine globale Lizenz; die lokale Lizenzangabe wird daher nur auf den erfassten pstack-Teil bezogen.

## Empfohlene Integrationsform

Als isolierte, Git-ignorierte Analysekopie behalten. Vor einer Installation oder Übernahme einzelner Skills deren konkrete Abhängigkeiten, Prompt-Rechte und Ausführungswege erneut prüfen und den Trust-Level in der Registry für den gewählten Scope dokumentieren.

## Offene Fragen

- Welcher einzelne Skill würde im eigenen Workflow einen messbaren Engpass lösen?
- Für welchen Ziel-Harness soll gegebenenfalls die generierte Adapterfassung geprüft werden?

**Philipp-Freigabe erforderlich:** Für die bereits beauftragte Referenzablage nein; vor einer produktiven Aktivierung ja.
