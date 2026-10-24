# Sicherer Fallback vor menschlicher Eskalation

**Konfidenz:** meinung

## Zweck

Begrenzte Agent-Autonomie so entwerfen, dass ein unmittelbarer Fehlerpfad nicht von der sofortigen Reaktion eines Menschen abhängt. Menschliches Urteil folgt auf die vorgesehene Schadensbegrenzung.

## Funktionsweise

Pro autonomer Arbeitsklasse zulässige Aufgaben, Voraussetzungen, Aktionen, Laufzeit und Budget festlegen. Dazu einen fachlich geeigneten sicheren Zustand und einen erlaubten Weg dorthin entwerfen: vor weiteren Aktionen stoppen, den betroffenen Prozess isolieren oder einen vorgesehenen Zustand wiederherstellen. Den Fehlerpfad vor Erweiterung der Autonomie prüfen.

Bei Störungen den vorbereiteten Fehlerpfad innerhalb der autorisierten Rechte ausführen und danach mit Zustand, Befunden und verbleibenden Auswirkungen menschlich eskalieren. Aufgaben ohne tragfähigen Fallback bleiben außerhalb der autonomen Klasse. Wiederherstellbarkeit wird weder aus einem Git-Revert noch einem theoretischen Rollback abgeleitet.

## Vorteile

- Macht Fehlerbehandlung und Eskalation zu getrennten, prüfbaren Entwurfsentscheidungen.
- Begrenzt Autonomie nach Arbeitsklasse statt über ein pauschales Reifelabel.

## Nachteile & Grenzen

- Ein sicherer Zustand hängt vom Fachprozess und bereits entstandenen Wirkungen ab.
- Destruktive Migrationen, Datenverluste und externe Aktionen können irreversibel sein; späteres Stoppen macht sie nicht rückgängig.
- Die Quelle liefert ein Entwurfskriterium ohne Zuverlässigkeitsmessung oder allgemeine Freigabeschwelle.

## Wann einsetzen, wann nicht

- Einsetzen: abgegrenzte Abläufe mit erkennbarem Fehlerzustand und geprüftem, autorisiertem Rückfallweg.
- Nicht einsetzen: wenn nur sofortige menschliche Übernahme den Schaden begrenzen könnte oder der sichere Zustand unbekannt ist.

## Belege

- 2026-10-22 · [[2026-10-22-itamar_mar-2113255396299128887]] · meinung — Friedman unterscheidet L3 und L4 in seiner Softwareanalogie anhand des Fehlerpfads: L4 stoppt, isoliert oder stellt sicher wieder her und eskaliert danach. Das ist ein vorgeschlagenes Entwurfskriterium pro Workflow, kein Standard und kein demonstrierter Betriebsnachweis.

## Spannungen & offene Fragen

- 2026-10-24 · [[2026-10-22-itamar_mar-2113255396299128887]]: Das Erreichen eines sicheren Zustands kann zusätzliche Aktionen erfordern; diese brauchen selbst begrenzte Rechte und einen geprüften Scope. Ein geplanter Fallback legitimiert keine ungefragten destruktiven Änderungen.

## Verwandte Patterns

- [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]]
- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]]
- [[Freigaben-und-Isolation-getrennt-steuern]]
