# Lokale Inferenz nach Arbeitslast dimensionieren

**Konfidenz:** meinung

## Zweck

Den Rechner für lokale KI anhand der benötigten Aufgabe und beobachteten Laufzeit beurteilen, statt allein aus einer passenden Modelldateigröße oder einer theoretischen Bandbreite auf Eignung zu schließen.

## Funktionsweise

Stand der Ausarbeitung: 2026-10-11. Die Einführung vom 2026-09-01 beginnt mit Aufgabe und erforderlicher Qualität. Danach folgen Modell, Quantisierung, Kontextlänge und gleichzeitige Sitzungen. Modellgewichte, zusätzlicher Kontext- und Laufzeitspeicher sowie der übrige Systembedarf werden getrennt betrachtet.

Ein repräsentativer Versuch prüft tatsächliche Speicherspitze, Promptverarbeitung, Ausgabe und vollständige Agentenlaufzeit. Laufzeitumgebung und Einstellungen werden vor einer Hardwareerweiterung betrachtet. Erst danach folgt der Vergleich des Gesamtaufwands mit dem bestehenden Arbeitsweg; der Autor empfiehlt auch einen begrenzten Hardwareversuch vor der Anschaffung.

Konkrete Geräte, Preise und Tokenraten des Videos bleiben historische Beispiele. Die automatische Abschrift enthält widersprüchliche Rechen- und Begriffsstellen. Ein universeller Speicheraufschlag oder eine pauschale Leistungsformel wird daraus nicht abgeleitet. Das Verfahren ergänzt die lokale Modell-Umleitung um die Prüfung des tatsächlich dahinterliegenden Arbeitswegs.

## Vorteile

- Verbindet Kapazitätsplanung mit der benötigten Ergebnisqualität.
- Unterscheidet das Laden eines Modells von einer brauchbaren vollständigen Aufgabenlaufzeit.
- Macht Kontextlänge und gleichzeitige Arbeit zu ausdrücklichen Versuchsbedingungen.

## Nachteile & Grenzen

- Repräsentative Versuche benötigen Zeit und eine passende Arbeitslast.
- Ergebnisse hängen von Modellarchitektur, Quantisierung, Laufzeit und Parallelität ab.
- Die Quelle dokumentiert keinen vollständig vergleichbaren Gerätebenchmark und liefert keine aktuelle Kaufberatung.
- Lokaler Betrieb allein belegt weder fehlende Limits noch vollständig lokale Datenflüsse oder gleiches Modellverhalten.

## Wann einsetzen, wann nicht

- Einsetzen: vor dem Wechsel eines konkreten Agenten- oder Wissensarbeitsablaufs auf lokale Inferenz.
- Nicht einsetzen: als pauschale Geräterangliste oder als Ersatz für die Prüfung der tatsächlichen Aufgabenqualität.

## Belege

- 2026-09-01 · [[2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware]] · meinung — Der Autor empfiehlt Aufgabe, Modell, Kontext, Instanzen, Speicherbedarf und Geschwindigkeit vor dem Preisvergleich sowie einen praktischen Versuch vor der Anschaffung. Leistungswerte und pauschale Quantisierungsverluste wurden nicht unabhängig geprüft.

## Spannungen & offene Fragen

- 2026-10-11: Große Speicherkapazität kann ein Modell laden lassen, ohne eine für den vollständigen Arbeitsweg akzeptable Geschwindigkeit zu sichern. Theoretische Bandbreite ersetzt diesen Versuch nicht.
- 2026-10-11: Die gezeigten Zahlen und uneindeutigen Formeln sind kein gemeinsamer Benchmark. Für einen konkreten Wechsel fehlen vergleichbare Angaben zu Modell, Runtime, Kontext, Parallelität und Qualität.

## Verwandte Patterns

- [[Lokale-Modell-Umleitung-Muster]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Testharness-als-staerkster-Hebel]]
