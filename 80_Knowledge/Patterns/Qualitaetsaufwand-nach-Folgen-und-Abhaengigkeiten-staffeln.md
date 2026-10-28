# Qualitätsaufwand nach Folgen und Abhängigkeiten staffeln

**Konfidenz:** meinung

## Zweck

Prüftiefe und Entwicklungsaufwand anhand der tatsächlichen Folgen eines Softwarefehlers begründen.

## Funktionsweise

Beantworte vor der Umsetzung vier Fragen: Was folgt aus einem Ausfall? Was kostet ein Neubau? Welche Menschen oder Systeme hängen davon ab? Wie viel Wartung ist zu erwarten? Sprogis vermittelt diese Fragen aus einem Talk von Max Kanat-Alexander als Raster zwischen kurzlebigen Hilfswerkzeugen und langlebigen Produkten.

Die Ausarbeitung vom 28.10.2026 leitet daraus ab, Erfolgskriterien, Prüftiefe und Wiederherstellungsvorgehen ausdrücklich festzulegen. Werden weitere Daten, Nutzer oder abhängige Systeme angebunden, ist die Einstufung erneut zu prüfen. Gemeinsame automatische Checks können wiederholte Arbeit erleichtern; die Quelle liefert keine kalibrierten Schwellen oder gemessene Aufwandsersparnis.

## Vorteile

- Verbindet Qualitätsentscheidungen mit konkreten Fehlerfolgen statt allein mit der Größe des Codes.
- Macht Abhängigkeiten und Wiederherstellungskosten vor einer Ausweitung sichtbar.
- Liefert eine verständliche Grundlage für die Auswahl zusätzlicher Prüfungen.

## Nachteile & Grenzen

- Fehlerfolgen und Abhängigkeiten können anfangs unbekannt oder unterschätzt sein.
- Geringe Neubaukosten begrenzen weder Datenverluste noch Auswirkungen vorhandener Zugriffsrechte.
- Die vier Fragen liefern eine Heuristik, keine Messung einer sicheren Risikoschwelle.
- Automatisierte Checks müssen gepflegt und selbst auf Aussagekraft geprüft werden.

## Wann einsetzen, wann nicht

- Einsetzen: zur Begründung des Prüf- und Wartungsumfangs und beim Übergang eines internen Werkzeugs zu breiterer Nutzung.
- Nicht einsetzen: als Freistellung von konkreten Akzeptanzkriterien oder als pauschale Erlaubnis, Qualität bei Wegwerfsoftware zu ignorieren.

## Belege

- 2026-10-25 · [[2026-10-25-alex-sprogis-die-qualitaet-von-ki-code-ist-nicht-so-gut-wie-d]] · meinung — Sprogis ordnet Entwicklungsqualität über Ausfallfolgen, Neubaukosten, Abhängigkeiten und Wartung ein und übernimmt das Raster aus einem verlinkten Talk. Die Methode ist eine sekundär vermittelte Heuristik ohne gemessene Wirksamkeit oder universelle Schwellen.

## Spannungen & offene Fragen

- 2026-10-28: Die pauschale Entwarnung des Videos für Wegwerfsoftware wird nicht übernommen. Auch ein schnell ersetzbares Werkzeug kann folgenreiche Aktionen ausführen; die konkreten Folgen zählen zur Einstufung.

## Verwandte Patterns

- [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Testharness-als-staerkster-Hebel]]
- [[Produktreife-durch-echte-Testnutzer]]
