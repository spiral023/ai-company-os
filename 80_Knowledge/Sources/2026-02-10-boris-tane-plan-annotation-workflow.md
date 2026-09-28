---
url: https://boristane.com/blog/how-i-use-claude-code/
autor: "Boris Tane"
datum: 2026-02-10
erfasst: 2026-08-05
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-08-05-boristane-how-i-use-claude-code.md
zweitquelle: 00_Inbox/Quellen/URL/2026-02-10-boris-tane-boris-tane-claude-code-workflow.md
---

# Der Annotations-Zyklus: Plan als geteilter Zwischenzustand zwischen Mensch und Claude

Boris Tane nutzt Claude Code seit rund neun Monaten als primäres Entwicklungswerkzeug und beschreibt einen Workflow, der bewusst gegen den verbreiteten „Prompt, Fix, Wiederholen“-Reflex arbeitet. Sein Kernprinzip: **Claude schreibt niemals Code, bevor ein schriftlicher Plan geprüft und freigegeben ist.** Diese Trennung von Planung und Ausführung sei der wichtigste einzelne Hebel seiner Arbeitsweise — sie verhindere verschwendete Arbeit, halte ihn in Kontrolle über Architektur-Entscheidungen und liefere bei minimalem Tokenverbrauch deutlich bessere Ergebnisse als der direkte Sprung in den Code.

## Recherche als eigenständiges, geprüftes Artefakt

Jede nennenswerte Aufgabe beginnt mit einer expliziten Deep-Read-Anweisung. Boris verlangt, dass die Ergebnisse zwingend in eine persistente `research.md` geschrieben werden, nie nur als mündliche Zusammenfassung im Chat. Entscheidend ist dabei die Wortwahl: Formulierungen wie „deeply“, „in great details“ oder „intricacies“ seien keine Stilfrage, sondern ein notwendiges Signal — ohne sie liest Claude nur oberflächlich, erfasst Funktionssignaturen und geht weiter. Die `research.md` dient als Review-Fläche: Boris liest sie, prüft, ob Claude das System tatsächlich verstanden hat, und korrigiert Missverständnisse, bevor überhaupt geplant wird. Sein Prinzip dazu: „If the research is wrong, the plan will be wrong, and the implementation will be wrong. Garbage in, garbage out.“ Der teuerste Fehlermodus bei KI-gestütztem Coding sei nicht falsche Syntax, sondern Implementierungen, die isoliert funktionieren, aber das Gesamtsystem stören — eine Funktion, die eine bestehende Caching-Schicht ignoriert, eine Migration, die die Konventionen des ORM missachtet, ein Endpunkt, der bereits vorhandene Logik dupliziert. Genau das soll die Recherchephase verhindern.

## Der Annotations-Zyklus als Herzstück

Nach der Recherche folgt eine eigene `plan.md` in einer separaten Datei — bewusst nicht der eingebaute Plan Mode von Claude Code, den Boris als unzureichend beschreibt („the built-in plan mode sucks“), weil die eigene Markdown-Datei volle Kontrolle gibt, im Editor bearbeitbar ist und als reales Artefakt im Projekt bleibt. Ein Kniff dabei: Für gut abgegrenzte Features, zu denen er eine gute Open-Source-Implementierung kennt, fügt er den Referenzcode direkt der Planungsanfrage bei (z. B. eine Sortable-ID-Implementierung aus einem fremden Projekt) — Claude arbeite danach deutlich zielgerichteter, als wenn es komplett neu entwerfen müsse.

Der eigentliche Wertschöpfungsschritt ist die Annotation: Nachdem Claude die `plan.md` geschrieben hat, öffnet Boris sie im Editor und trägt Notizen direkt inline ein — Korrekturen von Annahmen, Ablehnungen von Ansätzen, fachliches Domänenwissen. Die Notizen variieren stark in Länge, von zwei Wörtern („not optional“) bis zu ganzen Absätzen mit Code-Beispielen. Konkrete Beispiele aus dem Artikel:

- „use drizzle:generate for migrations, not raw SQL“ — Domänenwissen, das Claude nicht hat
- „no — this should be a PATCH, not a PUT“ — Korrektur einer falschen Annahme
- „remove this section entirely, we don't need caching here“ — Ablehnung eines vorgeschlagenen Ansatzes
- „the queue consumer already handles retries, so this retry logic is redundant. remove it and just let it fail“ — Begründung für eine Änderung
- „this is wrong, the visibility field needs to be on the list itself, not on individual items … restructure the schema section accordingly“ — Umleitung eines ganzen Planabschnitts

Danach schickt er Claude mit einem festen Prompt zurück zum Dokument: „I added a few notes to the document, address all the notes and update the document accordingly. don't implement yet.“ Dieser Zyklus wiederholt sich nach eigener Angabe **ein bis sechs Mal**. Der explizite „don't implement yet“-Guard sei essenziell — ohne ihn springe Claude zur Implementierung, sobald der Plan aus seiner Sicht gut genug wirkt. Die Markdown-Datei fungiert dabei als **Shared Mutable State**: Boris kann in seinem eigenen Tempo denken, präzise an der fehlerhaften Stelle annotieren und ohne Kontextverlust wieder einsteigen — im Gegensatz zu einer Chat-Konversation, die man erst zurückscrollen müsste, um Entscheidungen zu rekonstruieren. Vor der Implementierung verlangt er zusätzlich eine granulare Todo-Liste im Plandokument, die Claude während der Arbeit selbst als Fortschrittstracker pflegt.

## Vom Architekten zum Supervisor

Ist der Plan fertig, nutzt Boris einen wiederverwendeten Standard-Prompt: „implement it all. when you're done with a task or phase, mark it as completed in the plan document. do not stop until all tasks and phases are completed. do not add unnecessary comments or jsdocs, do not use any or unknown types. continuously run typecheck to make sure you're not introducing new issues.“ Jeder Teil kodiert eine eigene Absicht: vollständige statt selektiver Umsetzung, der Plan als Fortschritts-Wahrheitsquelle, kein Zwischenstopp für Rückfragen, sauberer Code ohne unnötige Kommentare, strikte Typisierung, laufende Typprüfung statt Prüfung erst am Ende.

Während der Ausführung wechselt Boris' Rolle vom Architekten zum Supervisor, und seine Korrekturen werden dramatisch kürzer — Beispiele: „You didn't implement the deduplicateByTitle function.“ oder „You built the settings page in the main app when it should be in the admin app, move it.“ Bei Frontend-Arbeit testet er im Browser und gibt knappe Rückmeldungen wie „wider“, „still cropped“, „there's a 2px gap“, teils ergänzt durch Screenshots. Häufig verweist er auf bestehenden Code statt Anforderungen neu zu beschreiben: „this table should look exactly like the users table, same header, same pagination, same row density.“ Geht etwas grundsätzlich in die falsche Richtung, patcht er nicht nach, sondern verwirft die Git-Änderungen vollständig und grenzt den Scope neu ein — nach seiner Erfahrung liefere ein enger gefasster Neustart fast immer bessere Ergebnisse als der Versuch, einen schlechten Ansatz schrittweise zu reparieren.

## In der Fahrerkabine bleiben

Auch wenn Claude die Ausführung übernimmt, gibt Boris ihm nie vollständige Autonomie über das Was. Er unterscheidet vier Arten von Eingriffen in Vorschläge: **Cherry-Picking** (einzelne Punkte einer Vorschlagsliste separat annehmen, ändern oder verwerfen — „for the first one, just use Promise.all … ignore the fourth and fifth ones, they're not worth the complexity“), **Scope-Trimming** (Nice-to-haves aktiv aus dem Plan streichen, um Scope Creep zu verhindern), **Schnittstellen-Schutz** (harte Vorgaben wie „the signatures of these three functions should not change, the caller should adapt, not the library“) und **technische Overrides** (direkte Vorgaben wie eine bestimmte Bibliotheksmethode statt einer selbstgeschriebenen Lösung). Sein Fazit: Claude übernehme die mechanische Ausführung, während die Werturteile — Produktprioritäten, Nutzerschmerzpunkte, akzeptable technische Trade-offs — beim Menschen blieben.

## Eine einzige lange Session

Boris führt Recherche, Planung und Implementierung bewusst in einer einzigen langen Session statt in getrennten Sessions durch. Er berichtet, die vielfach diskutierte Leistungsdegradation nach 50 % Kontextfenster-Auslastung nicht zu beobachten — im Gegenteil: Bis zum „implement it all“-Befehl habe Claude bereits die gesamte Session investiert, um Verständnis aufzubauen. Fülle sich das Kontextfenster, halte Claudes Auto-Compaction genug Kontext, um weiterzumachen, und das Plandokument als persistentes Artefakt überlebe die Kompaktierung in voller Genauigkeit — er könne Claude jederzeit wieder darauf verweisen.

## Einordnung

Beide Fassungen beschreiben denselben Workflow; die Primärquelle liefert die wörtlichen Prompts, Beispiel-Annotationen und den Fahrerkabine-Abschnitt in voller Ausführlichkeit, während die vibedeck-Sekundärquelle den Ablauf verdichtet und mit eigenen Konzeptnamen (Planning Cycle, Annotation Cycle, Shared Mutable State, Research Mode) vorab einordnet, ohne über die Primärquelle hinausgehende Inhalte beizutragen. Die Notiz stützt sich deshalb auf die Primärquelle; die Sekundärquelle bestätigt dieselben Aussagen unabhängig, zählt aber wegen gemeinsamer Ursprungsquelle nicht als zweite unabhängige Bestätigung.

Der Beitrag ist ein Erfahrungsbericht einer Einzelperson, keine Messung. Zahlen wie „ein bis sechs Annotationsrunden“ oder „15 Minuten Fehlaufbau ohne Planungsphase“ sind Boris' eigene, unbelegte Schätzwerte und sollten so gelesen werden. Der Kern — Plan als editierbares, geteiltes Artefakt statt Chat-Verlauf — deckt sich stark mit dem bereits mehrfach unabhängig belegten Pattern [[Plan-first-mit-getrenntem-Review]]; neu und konkret ist vor allem die Trennung von `research.md` und `plan.md` als zwei separate, aufeinanderfolgende Artefakte sowie der feste, wortidentische Implementierungs-Prompt.

Bemerkenswert ist die Spannung zu zwei bestehenden Patterns: [[Kontext-Hygiene-Entscheidungsbaum]] empfiehlt, bei Phasenwechseln (Recherche → Planung → Umsetzung) aktiv zwischen `/compact`, `/clear` oder neuer Session zu wählen, und nennt eine Context-Rot-Schwelle von etwa 300k–400k Tokens. Boris tut das Gegenteil — eine einzige durchlaufende Session über alle drei Phasen, ausdrücklich ohne beobachtete Degradation nach 50 % Fenstergröße. Das widerspricht der bisherigen Empfehlung nicht mit Zahlen, sondern mit einer gegenläufigen Erfahrungsangabe; wie beim bereits im Pattern vermerkten Cerebras-Widerspruch (Kompaktierung „gut genug“ über sehr lange Sessions) bleibt auch dies unbelegt und wird als weitere Gegenstimme, nicht als Auflösung der Spannung, festgehalten. Sein Revert-statt-Nachbessern bei falscher Richtung deckt sich dagegen mit der `rewind`-vor-Korrektur-Empfehlung desselben Patterns. Auch zu [[Task-basierte-Steuerung]] besteht ein Gegensatz in der Grundhaltung: Jenes Pattern positioniert sich explizit gegen den „linearen Dreischritt Research → Plan → Implement“ — Boris' Workflow ist ein weiteres, unabhängiges Beispiel für genau diesen linearen, disziplinierten Ablauf und bestätigt damit die dort bereits dokumentierte Spannung von einer dritten Seite.

## Kernaussagen

- Nie Code schreiben lassen, bevor ein geschriebener, freigegebener Plan existiert; Recherche und Planung sind getrennte, persistente Markdown-Artefakte statt Chat-Verlauf → [[Plan-first-mit-getrenntem-Review]]
- Ohne explizite Deep-Read-Sprache („deeply“, „in great details“, „intricacies“) liest Claude nur oberflächlich bis zur Funktionssignatur → [[Plan-first-mit-getrenntem-Review]]
- Der Annotations-Zyklus (Plan als Shared Mutable State, inline Notizen, 1–6 Wiederholungen, „don't implement yet“-Guard) ist der wertschöpfende Schritt, nicht die erste Planversion selbst → [[Plan-first-mit-getrenntem-Review]]
- Nach Planfreigabe wechselt die Rolle vom Architekten zum Supervisor mit knappen Korrekturen; Rückschritte werden per Revert-und-Neuscoping statt Nachbesserung behandelt → [[Great-Decoupling-Rollenverstaendnis]] · [[Kontext-Hygiene-Entscheidungsbaum]]
- Menschliche Steuerung bleibt granular erhalten: Cherry-Picking einzelner Vorschläge, Scope-Trimming, Schnittstellenschutz und technische Overrides statt vollständiger Autonomie für den Agenten → [[Great-Decoupling-Rollenverstaendnis]]
- Eine einzige lange Session über Recherche, Planung und Implementierung zeigt laut Erfahrungsbericht keine Degradation nach 50 % Kontextfenster, weil das persistente Plandokument die Kompaktierung überlebt → [[Kontext-Hygiene-Entscheidungsbaum]] · [[Handoff-Doc]]

## Verbindungen

- [[Plan-first-mit-getrenntem-Review]]
- [[Great-Decoupling-Rollenverstaendnis]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Task-basierte-Steuerung]]
- [[Handoff-Doc]]
