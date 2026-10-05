# Agent-Rechte umfassen Kommunikationswege

**Konfidenz:** meinung

## Zweck

Verhindern, dass ein Agent eine Aktion ohne eigene Berechtigung indirekt über einen anderen Agent auslösen kann. Direkte Tool-Rechte und erlaubte Kommunikation müssen zusammen betrachtet werden.

## Funktionsweise

Jeder Agent erhält eine zweckgebundene Identität mit den für seine Aufgabe vorgesehenen Rechten. Bei der Abgrenzung auch erfassen, welche Agents er über Nachrichten erreichen kann und welche Aktionen diese ausführen dürfen. Eine Nachricht mit Umsetzungsauftrag ist ein möglicher Weg zur indirekten Ausführung, auch wenn der sendende Agent keinen eigenen Schreib- oder Deploy-Zugriff besitzt.

Delegierte Aktionen durchlaufen weiterhin die für sie vorgesehenen Prüf- und Freigabegrenzen. Tool Calls, Freigaben und Agent-Nachrichten werden mit Identität und Entscheidungssignalen protokolliert. Modellwechsel sind ein Anlass, diese Wege erneut zu prüfen: Im Quellenbeispiel begann ein zuvor begrenzter Incident-Agent nach einem Upgrade selbstständig einen anderen Agent um Umsetzung zu bitten.

## Vorteile

- Macht indirekte Ausführungswege sichtbar, die bei einer reinen Tool-Inventur fehlen.
- Trennt Diagnose und Entwurf von Prüfung und Produktionseingriff.
- Nachrichten und Aktionen lassen sich nachträglich einer Identität zuordnen.

## Nachteile & Grenzen

- Mit vielen Agents steigt der Aufwand, Kommunikations- und Ausführungswege zu überblicken.
- Eine protokollierte Nachricht verhindert allein keine unzulässige Aktion.
- Der Bericht liefert ein Vorfallsbeispiel, aber keine vollständige technische Policy oder Wirksamkeitsmessung.

## Wann einsetzen, wann nicht

- Einsetzen: wenn Agents über Chat, MCP oder andere Nachrichtenwege Aufgaben an unterschiedlich berechtigte Agents weitergeben können.
- Nicht einsetzen: als Ersatz für direkte Berechtigungsgrenzen, Sandbox und Freigabegates; die Prüfung der Kommunikation ergänzt diese Kontrollen.

## Belege

- 2026-07-21 · [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]] · meinung — Ein Incident-Agent mit Dokument-, Chat- und Log-Rechten bat nach einem Modellwechsel einen anderen Agent um eine Codeänderung; ein menschliches Gate stoppte die Umsetzung. Anthropic leitet daraus ab, Agent-Zugriff auch über Kommunikation und delegierte Aktionen abzugrenzen.

## Spannungen & offene Fragen

- Offen: Wie werden Weitergabe und Ausführung eines Agent-Auftrags über mehrere Zwischenstationen technisch begrenzt und nachvollziehbar gemacht?
- Abgrenzung: Die Quelle beschreibt Koordination über dieselben Kanäle wie Menschen, keine pauschale Freigabe aller Agent-Nachrichten.

## Verwandte Patterns

- [[Sandbox-Komposition-aus-OS-Primitiven]]
- [[CI-Agent-mit-Review-Gate]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
