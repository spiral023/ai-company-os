# RAG mit Text-, Tabellen- und Volltextpfad

**Konfidenz:** meinung

## Zweck

Fragen aus gemischten Dokumentenbeständen über einen passenden Zugriff beantworten. Eine ähnliche Textstelle genügt nicht für jede Frage: Summen brauchen strukturierte Daten, zusammenhängende Inhalte gegebenenfalls das vollständige Dokument.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-11. Das Tutorial vom 2025-09-22 verbindet Originaldateien und ihre Ableitungen über stabile Datei-IDs. OCR erschließt Dokumenttext und Bildverweise; Tabellen werden zusätzlich strukturiert gespeichert. Ein Agent erhält getrennte Werkzeuge für semantische Textsuche, das Nachladen eines vollständigen Dokuments und Datenbankabfragen auf Tabellen. Reranking bewertet die ausgewählten Texttreffer erneut.

Änderungen und entfernte Originale werden mit den zugehörigen Ableitungen abgeglichen. Die Identität einer Quelle verbindet dabei Metadaten, Textabschnitte, Tabellenzeilen und Bildverweise. Der konkrete Anbieterstack ist ein historisches Implementierungsbeispiel, keine Voraussetzung dieser Arbeitsweise.

Als abgeleiteter Prüfbedarf sollten Inhaltsfragen, Tabellenaggregationen und Bestandsänderungen getrennte Sollfälle erhalten. Das Video zeigt erfolgreiche Beispiele, aber keine solche systematische Evaluation. Auch der Wiederanlauf nach einem Teilfehler ist eigens zu prüfen: Ein bereits fortgeschriebener Synchronisationsstand belegt noch keinen vollständig aktualisierten Antwortbestand.

## Vorteile

- Verhindert, dass tabellarische Berechnungen allein durch ähnliche Textabschnitte beantwortet werden sollen.
- Quellenidentität macht Ableitungen und Aktualisierungen nachvollziehbar.
- Volltextzugriff kann Kontext ergänzen, den einzelne Chunks verlieren.

## Nachteile & Grenzen

- OCR, Chunking, Toolwahl und Abfragen können fehlerhaft sein; ein SQL-Zugriff garantiert keine richtige Antwort.
- Mehrere Datenpfade erhöhen Betriebs-, Synchronisations- und Prüfaufwand.
- Externe Dienste oder öffentlich erreichbare Bildlinks begründen keine allgemeine Datenschutzkonformität.
- Die Quelle basiert auf einem fremden Template und demonstriert Normalfälle; Wirksamkeit, Rechteprüfung und Wiederanlauf sind nicht umfassend belegt.

## Wann einsetzen, wann nicht

- Einsetzen: bei Wissensbeständen, die sowohl Dokumentinhalte als auch strukturierte Tabellenfragen enthalten.
- Nicht einsetzen: wenn eine einfache Dokumentensuche genügt oder Quellenzustand, Zugriffsrechte und Antwortqualität nicht überprüfbar sind.

## Belege

- 2025-09-22 · [[2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral]] · meinung — Ivanov demonstriert getrennte OCR-/Text- und Tabellenpfade, Reranking, Volltextnachladen sowie Aktualisierung und Entfernung über Datei-IDs. Das Tutorial basiert auf Cole Medins Template und ist kein unabhängiger Wirksamkeitsvergleich.

## Spannungen & offene Fragen

- 2026-10-11: Mehrere Zugriffspfade erweitern die Antwortmöglichkeiten, verlangen aber mehr Prüfung der Toolwahl und Konsistenz. Im gezeigten Ablauf werden Synchronisationszustand und alte Ableitungen früh verändert; eine belastbare Fehler- und Wiederanlaufstrategie bleibt offen.
- 2026-10-11: Beworbene Datenkontrolle steht einer konkreten Integration externer Dienste und öffentlich erreichbarer Bildlinks gegenüber. Die Demo ersetzt keine Prüfung des eigenen Einsatzes.

## Verwandte Patterns

- [[Action-Space-Design-nach-Modellfaehigkeit]]
- [[Testharness-als-staerkster-Hebel]]
- [[Intent-Engineering-als-dritte-Schicht]]
