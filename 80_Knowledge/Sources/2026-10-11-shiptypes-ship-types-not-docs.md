---
url: https://shiptypes.com/
autor: Boris Tane
datum: 2026-10-11
datum_unsicher: true
erfasst: 2026-10-11
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-11-shiptypes-ship-types-not-docs.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# API-Verträge aus einem Schema ableiten und in CI prüfen

Der Beitrag auf Ship types schlägt vor, maschinenlesbare Schemas als gemeinsamen Vertrag zwischen Services, Clients und Coding Agents zu pflegen. Typen, Validatoren und SDKs sollen daraus entstehen, damit Payloads nicht aus möglicherweise veralteter Prosa rekonstruiert werden. Der Autorenhinweis im archivierten Bild-Alttext nennt Boris Tane; das Original-Veröffentlichungsdatum fehlt, `2026-10-11` ist der unsichere Archivwert.

## Ein Vertrag, mehrere Darstellungen

Der gezeigte Ablauf beginnt mit einem Schema für Requests und Responses. Daraus werden TypeScript-Typen abgeleitet, eingehende Daten zur Laufzeit validiert und OpenAPI, Dokumentation sowie Clients generiert. Typed RPC oder gemeinsam versionierte Schema-Pakete tragen denselben Vertrag über Servicegrenzen.

CI regeneriert die Artefakte, prüft auf nicht eingecheckte Änderungen und führt Typechecks der Verbraucher aus. Für bestehende Systeme empfiehlt der Autor einen schrittweisen Einstieg an besonders häufig genutzten Endpunkten und typisierte Wrapper, statt eines vollständigen Architekturumbaus.

Als Werkzeuge nennt er Zod, Cloudflare JavaScript-native RPC, tRPC, Protocol Buffers und Smithy. Das sind Beispiele für unterschiedliche Stacks; die konkreten Codeschnipsel wurden in diesem Lauf nicht ausgeführt.

## Was Agents daraus gewinnen sollen

Ein Coding Agent kann Feldnamen, Pflichtfelder und erlaubte Werte direkt lesen. Das soll Fehler und Wiederholungsversuche verringern. Der Autor behauptet den Faktor `4×` für Tokenkosten und Latenz von Integrationen allein anhand von Dokumentation, legt aber keinen kontrollierten Versuch vor. Der Faktor ist daher keine belastbare Einsparungsprognose.

Prosa bleibt für Zweck, Einsatzbedingungen und Architekturzusammenhänge sinnvoll. Der Vorschlag betrifft vor allem die redundante Beschreibung struktureller Schnittstellenverträge.

## Einordnung

Das Schema als gemeinsame Quelle ist eine konkrete, wiederverwendbare Arbeitsweise; es ergänzt Fachregel-Konsolidierung um die Grenze zwischen Produzenten und Verbrauchern. Die Aussage, erfolgreicher Compile garantiere korrektes Verhalten, geht zu weit: Laufzeitdaten, Fachregeln, Berechtigungen und unabhängig ausgelieferte Versionen bleiben zu prüfen. Auch die frühe RPC-Demo enthält einen abweichenden Typnamen `CreateOrderRequest`, obwohl zuvor `CreateOrder` definiert wurde. CI muss die tatsächlich verwendeten Clients und Versionen prüfen; Generation allein verhindert keine semantischen Breaking Changes. Die Quelle ist ein Erfahrungs- und Meinungsbeitrag mit Produktwerbung, kein gemessener Vergleich.

## Kernaussagen

- Requests, Responses, Typen und Clients aus einer versionierten Schemaquelle ableiten → [[Schema-als-Vertrag-mit-generierten-Clients]]
- Regeneration und Typechecks der Verbraucher als CI-Gate ausführen → [[Schema-als-Vertrag-mit-generierten-Clients]]
- Strukturelle Verträge zentralisieren und Fachverhalten gesondert prüfen → [[Fachregel-Konsolidierung-vor-Featureaenderung]]

## Verbindungen

- [[Schema-als-Vertrag-mit-generierten-Clients]]
- [[Fachregel-Konsolidierung-vor-Featureaenderung]]
- [[Refactoring-mit-Verhaltensvergleich]]
