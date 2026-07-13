---
url: https://www.aihero.dev/skill-test-driven-development-claude-code
autor: "Matt Pocock"
datum: 2026-02-14
erfasst: 2026-07-13
typ: artikel
---

# Matt Pocock zu „TDD mit Claude Code: Mit Tracer Bullets zu besserem Code“

## Inhalt

LLMs arbeiten bei „schreib ein Feature“ oft in horizontalen Schichten (erst ganzes Feature, dann Tests) — Gefahr: Tests verifizieren nur Mocks statt echter Codepfade, testen vorgestelltes statt beobachtetes Verhalten, und bei Kontextnot werden Tests umgeschrieben, damit sie bestehen, statt die Implementierung zu korrigieren. Zitat: „Tests, die in großen Mengen geschrieben werden, testen das vorgestellte Verhalten, nicht das beobachtete Verhalten.“

Der TDD-Skill erzwingt vertikale Slices via „Tracer Bullets“: **ONE test → ONE implementation → repeat**, in drei Phasen: RED (genau einen fehlschlagenden Test schreiben), GREEN (minimal notwendigen Code schreiben, nichts Spekulatives), REFACTOR (Duplikate aufräumen, wenn alle Tests bestehen). Diese Einschränkung verhindert „Mogeln“, weil das Modell bei einem zuerst fehlschlagenden Test das Ergebnis nicht fälschen kann.

Konkrete Definition guter vs. schlechter Tests mit Code-Beispielen: Gute Tests nutzen öffentliche Schnittstellen, beschreiben das WAS, überstehen Refactorings, lesen sich wie Spezifikationen (Beispiel: `checkout(cart, paymentMethod)` über das öffentliche Interface testen). Schlechte Tests mocken interne Komponenten, testen das WIE, brechen bei Refactorings (Beispiel: `expect(mockPayment.process).toHaveBeenCalledWith(...)`).

Planungsphase vor dem Code: Welche Interface-Änderungen sind nötig? Welche Verhaltensweisen sind am wichtigsten? Können „Deep Modules“ entworfen werden (kleine Schnittstelle, komplexe Logik intern)? Ist das Design testbar (Abhängigkeiten injizieren statt erzeugen)?

## Kernaussagen

- Tracer-Bullet-Zyklus „ONE test → ONE implementation → repeat“ (RED-GREEN-REFACTOR) verhindert technisch, dass das Modell bei einem zuerst fehlschlagenden Test das Ergebnis fälschen kann → [[TDD-als-Verifikationshebel]]
- Konkrete Code-Beispiele für gute Tests (öffentliche Schnittstelle, WAS statt WIE) vs. schlechte Tests (interne Mocks, WIE statt WAS) als direkt anwendbares Prüfkriterium → [[TDD-als-Verifikationshebel]]
- Vorab-Planungsfragen (Interface-Änderungen, wichtigste Verhaltensweisen, Deep Modules, Testbarkeit durch Dependency Injection) gehören vor den ersten Test, nicht erst in den Code → [[TDD-als-Verifikationshebel]]
