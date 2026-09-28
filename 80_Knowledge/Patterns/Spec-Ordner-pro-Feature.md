# Spec-Ordner-pro-Feature

**Konfidenz:** meinung

## Zweck

Gibt jedem Feature ein dauerhaftes, dateibasiertes Gedächtnis, das Session- und Kontextgrenzen überlebt und getrennt hält, was sonst leicht vermischt: die Zielsetzung (Warum/Was), den Fortschritt (Wo stehen wir), das Warum hinter einzelnen Entscheidungen und wiederverwendbares Handwerkszeug. Anders als ein einmaliges Handoff-Dokument oder ein einzelner Plan ist dieser Ordner auf die gesamte Lebensdauer eines Features angelegt, nicht auf eine Session oder eine einzelne Planungsphase.

## Funktionsweise

Pro Feature entsteht ein fester Satz von fünf Dateien in einem git-unsichtbaren (z. B. per Symlink eingebundenen) Verzeichnis: **`design.md`** als Source of Truth, zwischen Mensch und Agent abgestimmt, bevor überhaupt Code entsteht („Keine Spec, keine Implementierung“); **`implementation.md`** als Fortschritts-Tracker (erledigt/blockiert), der die Session-Kontinuität trägt — stößt eine Konversation an ein Kontextlimit, macht der Agent anhand dieser Datei dort weiter, wo sie aufgehört hat; **`decisions.md`** als Rationale-Log, das festhält, warum eine Weichenstellung so und nicht anders getroffen wurde, für den Agenten wie für das „zukünftige Ich“ des Menschen; **`prompts.md`** als Bibliothek wiederverwendbarer Prompts für wiederkehrende Teilaufgaben am Feature (Resync mit der Codebase, Verfeinern, Review, Testen nach Änderung); **`future-work.md`** als Parkplatz für zurückgestellte Ideen. Die fünf Dateien werden dabei überwiegend vom Agenten selbst geschrieben und aktuell gehalten, nicht nur vom Menschen befüllt.

## Vorteile

- Trennt vier unterschiedliche Informationsarten (Ziel, Fortschritt, Warum, Werkzeug), die in einem einzigen Plan- oder Handoff-Dokument sonst leicht vermischt werden.
- Die Session-Kontinuität über `implementation.md` macht ein Feature robust gegenüber beliebig vielen Kontextlimit-Neustarts, ohne dass der Fortschritt neu erzählt werden muss.
- `decisions.md` bewahrt Kontext, der sonst nur im (verworfenen) Chatverlauf steckt und nach einem `/clear` unwiederbringlich verloren wäre.
- `prompts.md` senkt die Wiederholkosten für Teilaufgaben, die bei diesem Feature immer wieder anfallen.

## Nachteile & Grenzen

- Fünf feste Dateien pro Feature sind mehr Struktur- und Pflegeaufwand als ein einzelner Plan oder ein einmaliges Handoff-Dokument — lohnt sich erst bei Features mit spürbarer Lebensdauer.
- Bisher nur als Einzelfallbeschreibung belegt; keine Zahl dazu, ab welcher Feature-Größe sich der Strukturaufwand gegenüber einem einfacheren Artefakt auszahlt.
- Setzt Disziplin voraus, die Dateien tatsächlich aktuell zu halten — ein veraltetes `implementation.md` täuscht Fortschritt vor, den es nicht gibt.

## Wann einsetzen, wann nicht

- Einsetzen: Features, die sich über viele Sessions und ein hohes Risiko von Kontextlimit-Neustarts erstrecken, mit nennenswerten Architekturentscheidungen, die später nachvollziehbar bleiben müssen.
- Nicht einsetzen: kleine, in einer Session abschließbare Änderungen — dort reicht ein einzelnes Plan- oder Handoff-Dokument, der Fünf-Dateien-Aufwand wäre unverhältnismäßig.

## Belege

- 2026-01-14 · [[2026-01-14-ashpreetbedi-claude-code-spec-first]] · meinung — X-Thread-Aufarbeitung (über vibedeck-Sekundärfassung) beschreibt ein privates, per Symlink eingebundenes `specs/`-Repository mit den fünf Dateien `design.md`/`implementation.md`/`decisions.md`/`prompts.md`/`future-work.md` pro Feature am Beispiel des eigenen Agno-Repos.
- 2026-07-17 · [[2026-07-17-promptgefluester-ich-werd-gerade-extrem-dafuer-kritisiert-dass-ich-an-meine-videos-gesagt]] · meinung — Gegenposition zu kleinen Specs: eine monolithische 126-Seiten-Spezifikation; ohne Vergleich.

## Spannungen & offene Fragen

- Einzige bisherige Quelle, selbst nur als Sekundärfassung ohne geprüfte Primärquelle vorliegend — keine unabhängige Zweitbestätigung.
- Verhältnis zu [[Plan-first-mit-getrenntem-Review]] und [[Handoff-Doc]]: Dieses Pattern teilt die Grundidee (persistenter Plan, externes Gedächtnis über Kontextlimits) mit beiden, ist aber breiter (fünf statt ein bis zwei Dateien) und auf die gesamte Feature-Lebensdauer statt auf eine einzelne Planungsphase oder einen einzelnen Übergabepunkt angelegt — keine Dublette, sondern eine aufwendigere, dauerhaftere Umsetzung derselben Grundidee.

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Handoff-Doc]]
