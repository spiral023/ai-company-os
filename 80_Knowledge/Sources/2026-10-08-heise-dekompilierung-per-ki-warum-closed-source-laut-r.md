---
url: https://www.heise.de/news/Open-Source-Papst-Raymond-KI-setzt-Closed-Source-Software-ein-Ende-11480624.html
autor: "Malte Kirchner"
datum: 2026-10-08
erfasst: 2026-10-17
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-10-08-heise-dekompilierung-per-ki-warum-closed-source-laut-r.md
thema: Markt & Strategie
zeitkritisch: ja
---

# Technische Rekonstruierbarkeit beweist keinen Zusammenbruch proprietärer Software

Malte Kirchner berichtet bei Heise über Eric S. Raymonds Prognose, KI-gestütztes Reverse Engineering werde Closed Source weitgehend beenden. Es handelt sich um einen Sekundärbericht über Raymonds Meinungsbeiträge und ein von ihm beschriebenes Experiment, nicht um einen unabhängigen Nachweis eines Marktumbruchs. Besonders wichtig: Heise bezeichnet die behauptete Entstehung eines Photoshop-Ersatzes durch Dekompilierung ausdrücklich als bislang unbelegt.

## Die Beleglage reicht unterschiedlich weit

Raymonds Ausgangspunkt ist laut Bericht das DOS-Shareware-Spiel Firefighter. Er habe es mithilfe eines KI-Assistenten dekompiliert und anschließend nach Rust übertragen. Die KI habe das Borland-Pascal-Datenlayout erkannt und verständlichen Pascal-Code mit sinnvollen Namen ausgegeben. Diese Angaben werden durch Heise vermittelt; Implementierung, Originalvergleich und Testergebnisse wurden hier nicht geprüft.

Die nächste Stufe ist deutlich schwächer: Raymond habe inzwischen gehört, dass Vergleichbares mit vollständigen Triple-A-Spielen gelungen sei. Darauf folgt seine allgemeine Schlussfolgerung, praktisch keine lokal ausgelieferte Software sei mehr dauerhaft gegen Rekonstruktion geschützt. Der Artikel enthält weder einen vergleichenden Skalierungstest noch einen Nachweis dieser Verallgemeinerung.

Die Behauptung über einen dekompilierten Photoshop-Ersatz erhält sogar einen ausdrücklichen Vorbehalt des Berichts. Sie darf deshalb nicht als weiterer erfolgreicher Versuch neben Firefighter gezählt werden.

## Welche Wertquellen die Prognose selbst übrig lässt

Kirchner berichtet, Raymond sehe insbesondere Patente und serverseitig betriebene Software als verbleibenden Schutz proprietärer Geschäftsmodelle. Steuersoftware nennt Raymond als möglichen Sonderfall: Ihr Wert liege in der laufenden fachlichen Pflege veränderlicher Regeln.

Das ist für die strategische Einordnung nützlicher als das Kollapsbild: Die Quelle unterscheidet selbst zwischen rekonstruierbarem Programm und fortlaufend erbrachter Fachleistung. Aus einem lesbaren oder nachgebauten Artefakt folgt im Artikel kein gemessener Effekt auf Umsatz, Wechselkosten oder Zahlungsbereitschaft. Eine konkrete Markt- oder Beschaffungsentscheidung lässt sich damit nicht begründen.

## Gegenpositionen und verbleibende Grenzen

Der Bericht beschreibt Einwände gegen einen vollständigen Cloud-Umzug: Nutzerwiderstand und problematische Netzausfälle bei bestimmten Anwendungen. Er gibt zudem die differenziertere Position von Sicherheitsforschern wieder, nach der Obfuskierung zwar billiger zu überwinden sei, aber weiterhin einen Wert habe. Codesignierung und Secure Boot werden als Grenze zwischen Lesen und dem Ausführen veränderter Software auf gesperrter Hardware angeführt.

Diese Punkte betreffen unterschiedliche Ebenen: Untersuchung, Veränderung, Auslieferung und verlässlichen Betrieb. Sie sind im Artikel diskutierte Grenzen, keine hier geprüften Schutzmaßnahmen oder Belege für einen bestimmten Marktverlauf.

## Rechtsdarstellung bleibt eine ungeprüfte Quellenposition

Heise referiert Raymonds US-bezogene Vorstellung eines Ablaufs von Binärdatei über Spezifikation zu neuem Code sowie seine Einschätzungen zu Verfolgungspraktikabilität und Patenten. Der Artikel stellt dem eine strengere europäische Rechtsdarstellung gegenüber. Diese Aussagen und Rechtsverweise wurden für diese Notiz nicht unabhängig geprüft. Weder daraus noch aus einem technischen Rekonstruktionserfolg wird eine Handlungsfreigabe abgeleitet.

## Einordnung

Der Bericht ist ein Signal für eine aktuelle strategische Debatte, kein Kausal- oder Marktbeweis. Sein stärkster Beitrag ist die sichtbare Lücke zwischen einem berichteten Legacy-Experiment, weitergereichten Erfolgserzählungen und einer universellen Prognose. Für eine eigene Entscheidung müssten Zielsoftware, erforderliche Funktionen und überprüfbare Ergebnisse einzeln bestimmt werden. Der wirtschaftliche Wert fachlicher Pflege und verlässlichen Betriebs bleibt in der Quelle selbst ein Gegenargument gegen reine Codebetrachtung. Prognose und Nachrichtenstand sind zeitabhängig; Raymonds Originalbeiträge wurden hier nicht separat geprüft.

## Kernaussagen

- [[Testharness-als-staerkster-Hebel]]: Ein konkret beschriebenes Experiment und ein überprüfter Originalvergleich haben unterschiedliche Belegstärke; pauschale Skalierungsbehauptungen ersetzen keinen Verifier.
- Technische Nachbaubarkeit, produktiver Ersatz und wirtschaftlicher Bedeutungsverlust sind getrennte Behauptungen mit jeweils fehlenden Nachweisen.

## Verbindungen

- [[Testharness-als-staerkster-Hebel]] liefert den Prüfmaßstab für die Verallgemeinerung eines berichteten Erfolgs.
- [[2026-10-12-0xcodila-2109623431763292649]] diskutiert dieselbe Adobe-/Reverse-Engineering-Erzählung; Wiederholung bestätigt die behauptete Dekompilierung nicht unabhängig.
- [[2026-10-12-julian-ivanov-ki-automat-ki-kopiert-jetzt-jede-software-und-keiner-kann-e]] beschreibt den Adobe-Fall als äußeren Nachbau und nennt fehlende Funktionen; dies macht die abweichenden Entstehungserzählungen sichtbar, entscheidet aber nicht selbst, welche vollständig belegt ist.

Das lokale Titelbild wurde gesichtet: ein dekoratives Stockfoto mit Code auf Bildschirmen, ohne zusätzlichen Erklär- oder Belegwert. Es wird nicht eingebunden.
