# Claude-als-Lernwerkzeug

**Konfidenz:** meinung

## Zweck

Nutzt einen Coding Agent nicht nur zum Produzieren von Code, sondern gezielt zum Verstehen unbekannten Codes oder komplexer Protokolle. Adressiert die Lücke, dass Produktivitätsfokus und Lernfokus meist getrennt behandelt werden, obwohl derselbe Agent für beides eingesetzt werden kann.

## Funktionsweise

Statt eine Änderung direkt umsetzen zu lassen, wird der Agent explizit in einen erklärenden Modus versetzt: ein „Explanatory“- bzw. „Learning“-Stil (z. B. über `/config` einstellbar), der Erklärungen statt reiner Umsetzung liefert. Ergänzend lässt sich der Agent HTML-Präsentationen oder ASCII-Diagramme erzeugen, um komplexe Protokolle oder Code-Strukturen visuell aufzuschlüsseln. Ein weiterer Baustein ist ein selbstgebauter „Spaced-Repetition“-Skill, der das eigene Verständnis in wiederkehrenden Abständen abfragt und gezielt Wissenslücken schließt, statt einmalig erklärt und dann vergessen zu werden.

## Vorteile

- Macht Onboarding in unbekannten Code oder komplexe Protokolle schneller, weil der Agent aktiv erklärt statt nur zu implementieren.
- Diagramme/Visualisierungen senken die Einstiegshürde gegenüber reinem Fließtext bei komplexen Strukturen.
- Spaced Repetition wandelt einmalige Erklärung in nachhaltiges Verständnis um, statt dass Wissen nach der Session wieder verloren geht.

## Nachteile & Grenzen

- Zusätzlicher Aufwand (Moduswechsel, Diagramm-Anfrage, Spaced-Repetition-Skill selbst bauen) gegenüber dem reinen Produktivitätseinsatz.
- Kein Beleg dafür, wie genau oder verlässlich die Erklärungen des Agenten im Vergleich zu einer menschlichen Erklärung oder offizieller Dokumentation sind.
- Der Spaced-Repetition-Skill ist eine Eigenbau-Lösung ohne beschriebene Umsetzungsdetails — nicht direkt nachbaubar aus der Quelle allein.

## Wann einsetzen, wann nicht

- Einsetzen: Einarbeitung in unbekannte Codebasen, komplexe Protokolle oder Architekturen, bei denen Verständnis wichtiger ist als sofortige Umsetzung.
- Nicht einsetzen: reine Produktivaufgaben, bei denen das Ergebnis zählt und kein Lernbedarf besteht.

## Belege

- 2026-01-31 · [[2026-01-31-bcherny-claude-code-team-tips]] · meinung — Boris Chernys Team (laut Tweet-Sekundärquelle) nennt Claude Code als Lernwerkzeug für unbekannten Code als eigenständigen, vom reinen Produktivitätsfokus abweichenden zehnten Praxispunkt: Explanatory-/Learning-Stil, HTML-/ASCII-Diagramme, ein selbstgebauter Spaced-Repetition-Skill.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, unbelegte Team-Selbstauskunft ohne Beispiel oder Vorher-Nachher-Vergleich.
- Offene Frage: Wie verhält sich dieses Pattern zu [[Great-Decoupling-Rollenverstaendnis]], das bereits beschreibt, dass echtes System-Verständnis durch das Lesen von Agenten-Output entsteht — ist „Claude als Lernwerkzeug“ eine eigenständige Technik oder nur eine bewusste Zuspitzung derselben Grundidee auf den Lernfall?

## Verwandte Patterns

- [[Great-Decoupling-Rollenverstaendnis]]
