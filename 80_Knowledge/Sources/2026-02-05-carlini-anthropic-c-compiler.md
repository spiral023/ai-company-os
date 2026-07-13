---
url: https://www.anthropic.com/engineering/building-c-compiler
autor: "Nicholas Carlini (Anthropic)"
datum: 2026-02-05
erfasst: 2026-07-13
typ: artikel
---

# Nicholas Carlini (Anthropic) zu „Building a C compiler with a team of parallel Claudes“

## Inhalt

16 parallel laufende Claude-Agenten bauten in ca. zwei Wochen (knapp 2.000 Sessions, ~2 Mrd. Input-/140 Mio. Output-Tokens, ~20.000 USD) einen Rust-basierten C-Compiler mit ~100.000 Zeilen, der Linux 6.9 auf x86/ARM/RISC-V sowie mehrere große OSS-Projekte (QEMU, FFmpeg, SQLite, Postgres, Redis) baut.

Kernpunkte:
- **„Long-running Claudes“**: ein simpler Endlos-Loop (nach Aufgabenabschluss sofort zur nächsten) verhindert, dass ein Agent bei Unsicherheit stoppt und auf Instruktionen wartet — funktioniert aber nur, wenn Tests/Feedback/Projektstruktur klar genug sind.
- **Testharness statt besserer Prompt** ist der stärkste Hebel: Agenten optimieren zuverlässig das, was der Verifier misst — ist der Verifier unpräzise, wird der Agent zuverlässig „falsch erfolgreich“. Maßnahmen: hochwertige Test-Suites integrieren, Verifier/Build-Skripte für reale OSS-Projekte schreiben, Tests entlang beobachteter Fehlermuster ergänzen, CI verschärfen sobald Regressionen zunehmen.
- Tests müssen für Agenten designt werden, nicht für Menschen: klar, maschinenlesbar, präzise Fehlerlokalisierung statt „rot/grün“, damit auch kontextarme frische Agent-Instanzen schnell orientiert sind.
- Bei einem großen monolithischen Fehlerzustand (Linux-Kernel-Build) half Parallelität zunächst nicht (alle Agenten liefen gegen dasselbe Problem, Konflikte statt Fortschritt) — Lösung war ein **Oracle-Ansatz**: Teilmengen mit GCC, andere mit dem Claude-Compiler kompilieren, um den Suchraum schrittweise einzugrenzen.
- Spezialisierte Agentenrollen statt N identischer Bugfix-Agenten (Duplikat-Konsolidierung, Performance, Zielcode-Qualität, Rust-Designkritik, Doku) als Qualitätsmultiplikator.
- Explizit dokumentierte Grenzen: Regressionen blieben wiederkehrendes Problem, ein 16-bit-x86-Codegenerator für den Boot-Pfad war so schwer, dass auf GCC ausgewichen wurde — Hybridlösungen sind in der Praxis oft nötig.
- Sicherheitswarnung des Autors selbst: Wenn Menschen nicht mehr eng im Loop sind, steigt das Risiko, „alles grün“ fälschlich als „alles sicher“ zu lesen — Tests decken nie alle Angriffsflächen ab.

## Kernaussagen

- Der stärkste Hebel für autonome, lang laufende Agent-Teams ist ein präzises, maschinenlesbares Testharness — nicht ein besserer Prompt; ein unpräziser Verifier führt zu zuverlässig falschem Erfolg → [[Testharness-als-staerkster-Hebel]]
- Bei einem großen monolithischen Fehlerzustand hilft Parallelisierung erst, wenn ein Oracle (Referenzsystem wie GCC) den Suchraum in Teilprobleme zerlegt — sonst laufen alle Agenten gegeneinander → [[Testharness-als-staerkster-Hebel]], [[Kontrollierte-Agent-Parallelisierung]]
- Spezialisierte Agentenrollen (Qualität, Performance, Doku, Refactoring) statt identischer Bugfix-Agenten erhöhen den Ertrag von Parallelität deutlich → [[Kontrollierte-Agent-Parallelisierung]]
