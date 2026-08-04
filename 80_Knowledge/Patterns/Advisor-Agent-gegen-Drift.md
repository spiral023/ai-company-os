# Advisor-Agent-gegen-Drift

**Konfidenz:** meinung

## Zweck

Adressiert das Abdriften langer Agent-Läufe: Der Worker verliert über viele Schritte das ursprüngliche Ziel oder eine Nebenbedingung aus dem Blick und arbeitet plausibel, aber am Auftrag vorbei. Vorab-Planung und nachgelagertes Review greifen hier nicht — der Fehler entsteht *während* des Laufs und wird erst am Ende sichtbar, wenn die Arbeit schon getan ist.

## Funktionsweise

Ein zweiter Agent bekommt genau einen, eng umrissenen Auftrag: die laufende Session mitlesen, Ziel und Constraints im Gedächtnis behalten und eingreifen, sobald der Worker abweicht. Er arbeitet nicht mit, schreibt keinen Code und übernimmt die Aufgabe nicht — er beobachtet und stößt eine Kurskorrektur an.

Der Ablauf: Der Nutzer gibt die Aufgabe an den Worker. Der Worker arbeitet und streamt seine Session an den Advisor. Der Advisor prüft laufend auf Drift und schickt bei Abweichung einen Hinweis zurück. Der Worker korrigiert den Kurs und liefert das Ergebnis.

Entscheidend ist die Enge des Auftrags. Der Advisor hat kein Mandat für Qualitätsurteile, Stilfragen oder eigene Lösungsvorschläge — nur für die Frage, ob noch am Ziel gearbeitet wird. Diese Beschränkung ist der Grund, warum die Rolle mit einem günstigeren Modell besetzt werden kann als der Worker: Zieltreue überwachen ist eine leichtere Aufgabe als die Arbeit selbst.

## Vorteile

- Fängt Drift dort ab, wo sie entsteht, statt sie am Ende teuer zu reparieren.
- Die Rollentrennung ist billiger als sie klingt: der Advisor verarbeitet zwar die Session, produziert aber wenig Output und kann auf einem günstigen Modell laufen.
- Der explizite, enge Auftrag verhindert die typische Schwäche von Reviewer-Agenten, die alles kommentieren und dadurch nichts durchsetzen.
- Die überwachte Zielformulierung wirkt rückwirkend disziplinierend: Wer einen Advisor einsetzt, muss Ziel und Constraints vorab benennen können.

## Nachteile & Grenzen

- Zusätzliche Kosten und Latenz durch einen zweiten Modell-Aufruf über die gesamte Laufzeit; bei kurzen Aufgaben steht das in keinem Verhältnis.
- Der Advisor sieht nur, was gestreamt wird. Was der Worker intern verwirft oder nicht ausspricht, kann er nicht bewerten.
- Ein Advisor, der zu häufig eingreift, wird selbst zur Störquelle und kann den Worker in Schleifen treiben. Die Eingriffsschwelle ist der kritische Parameter und im Quellmaterial nicht quantifiziert.
- Setzt voraus, dass Ziel und Constraints überhaupt scharf formulierbar sind. Bei explorativen Aufgaben ohne festes Ziel gibt es keine Drift, die man messen könnte.

## Wann einsetzen, wann nicht

- Einsetzen: bei langlaufenden Aufgaben über viele Schritte, bei Arbeiten mit harten Nebenbedingungen (Budget, API-Kompatibilität, Sicherheitsvorgaben), und wenn wiederholt beobachtet wurde, dass Läufe plausibel aber am Auftrag vorbei enden.
- Nicht einsetzen: bei kurzen Aufgaben, bei explorativer Arbeit ohne festes Ziel, und wenn statt Zieltreue die fachliche Qualität geprüft werden soll — dafür ist ein nachgelagertes Review nach [[Plan-first-mit-getrenntem-Review]] das passende Mittel.

## Belege

- 2026-07-27 · [[2026-07-27-cerebras-gpt-5-6-modellwahl-und-reasoning]] · meinung — Cerebras-Artikel beschreibt den „Advisor workflow“ als Rolle mit genau einem Auftrag (vollständige Session lesen, Ziel und Constraints halten, bei Drift eingreifen); das mitgelieferte Sequenzdiagramm zeigt den Ablauf Task → Work → Stream session → Watch for drift → Nudge when off-program → Correct course → Result.

## Spannungen & offene Fragen

- Bisher eine Quelle, ohne Messung des Nutzens. Behauptet wird „improve reliability across longer tasks“, ohne Vergleichszahlen gegen einen Lauf ohne Advisor.
- Verhältnis zu [[Plan-first-mit-getrenntem-Review]] ist komplementär, nicht konkurrierend: dort getrennte Rollen vor und nach der Arbeit, hier eine Rolle *während* der Arbeit. Ob sich beides kombinieren lässt, ohne dass sich Plan, Advisor und Reviewer widersprechen, ist offen.
- Offene Frage: Wie wird die Eingriffsschwelle festgelegt? Ohne Schwellenwert bleibt unklar, wie man einen nützlichen Advisor von einem störenden unterscheidet.

## Verwandte Patterns

- [[Plan-first-mit-getrenntem-Review]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[Modell-Eskalation-von-guenstig-nach-teuer]]
- [[Testharness-als-staerkster-Hebel]]
