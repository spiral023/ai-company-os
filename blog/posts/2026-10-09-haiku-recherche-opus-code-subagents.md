---
titel: "Haiku für Recherche, Opus für Code: Subagents sinnvoll aufteilen"
datum: 2026-10-09
kategorie: arbeitsweisen
zusammenfassung: "Teile Claude-Code-Subagents nach prüfbaren Aufgaben auf: Haiku recherchiert, Opus integriert und setzt um. Mit kleiner Recherche-Konfiguration und einem fairen Vergleich der Gesamtkosten."
status: freigegeben
geprueft_am: 2026-10-09
freigabe: automatisch
quellen:
  - 2026-10-08-voxyz_ai-haiku-subagents-und-opus-worker
  - 2026-01-06-jarrodwatts-context-engineering-guide
---

## Kurz gesagt

- Starte mit einer klar abgegrenzten Rechercheaufgabe für Haiku und lasse das Hauptmodell die Umsetzung übernehmen.
- Beschränke den Recherche-Agent auf lesende Werkzeuge und verlange nachvollziehbare Fundstellen.
- Prüfe vor dem Versuch die aktive Agent-Definition, Modellwahl und Effort-Einstellungen.
- Vergleiche Gesamtkosten, Nacharbeit, Tests und Ergebnisqualität, bevor du die Aufteilung zum Standard machst.

## Welche Arbeit kannst du sinnvoll abgeben?

Wenn dein Agent mehrere Dateien durchsucht, bevor er eine Änderung schreibt, lässt sich diese Recherche oft als eigener Auftrag formulieren. Geeignet wäre: „Finde die bestehende Exportfunktion, ihre Aufrufer und die dazugehörigen Tests.“ Weniger geeignet wäre: „Entscheide über unsere nächste Architektur und bereite alles vor.“ Der zweite Auftrag enthält bereits weitreichende Urteile.

Vox schlägt am 8. Oktober 2026 eine Rollenteilung für Claude Code vor: Haiku liest Code und recherchiert Dokumentation; Opus plant, führt Ergebnisse zusammen und übernimmt Änderungen und Tests. Das ist ein Praxisvorschlag. Der Beitrag misst diesen Ablauf nicht an einer Reihe vergleichbarer Coding-Aufgaben.{q:1}

Ein Subagent ist ein spezialisierter KI-Assistent mit eigenem Arbeitskontext. Jarrod Watts beschreibt bereits am 6. Januar 2026 einen Recherche-Agent, der Dokumentation durchsucht und nur eine verdichtete Zusammenfassung an die Hauptsession zurückgibt. Übertragbar ist die Übergabe eines begrenzten Ergebnisses. Die damalige Modellkonfiguration ist eine historische Momentaufnahme.{q:2}

Für deinen ersten Versuch empfehle ich Code-Recherche im eigenen Projekt. Du kannst die Fundstellen dort unmittelbar kontrollieren und brauchst keine zusätzlichen Webwerkzeuge. Das Hauptmodell entscheidet anschließend, ob die gefundenen Informationen für die Umsetzung ausreichen.

## Eine kleine Recherche-Konfiguration

Das folgende Beispiel ist ein Vorschlag für einen lokalen Versuch. Prüfe vorhandene Definitionen, bevor du die Datei `.claude/agents/Explore.md` anlegst. Gleichnamige Agents verdienen besondere Aufmerksamkeit.

```yaml
---
name: Explore
description: Findet vorhandene Implementierungen und zugehörige Tests.
tools: Read, Grep, Glob
model: haiku
effort: medium
---
Recherchiere die konkret beauftragte Frage im vorhandenen Code.
Liefere relevante Dateien und Zeilen, den bestehenden Ablauf
und offene Fragen. Trenne gefundene Aussagen von Vermutungen.
Schlage keine Umsetzung ohne nachvollziehbare Fundstellen vor.
```

`Read` liest Dateien, `Grep` sucht Text, `Glob` findet Dateipfade. Diese Werkzeugauswahl enthält weder Schreibwerkzeuge noch eine Shell. `effort` steuert den Rechenaufwand des Modells; die verfügbaren Stufen hängen vom Modell ab.

Laut [Claude-Code-Dokumentation zu Subagents](https://code.claude.com/docs/en/sub-agents), geprüft am 9. Oktober 2026, verwendet der eingebaute `Explore` in einer Opus-Hauptsession deren Modell. Ein eigener Agent mit dem Namen `Explore` ersetzt ihn. Projektdefinitionen haben Vorrang vor User-Definitionen. Ein beim Aufruf übergebenes Modell kann das `model`-Feld übersteuern; `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` kann eine globale Modellwahl erzwingen. `CLAUDE_CODE_EFFORT_LEVEL` hat Vorrang vor dem agentbezogenen Effort. Kontrolliere während eines Laufs mit `/tasks`, welches Modell und welcher Effort tatsächlich angezeigt werden.

Die Aliasse `haiku` und `opus` vermeiden eine festgeschriebene Versionsnummer im Beispiel. Halte für einen Vergleich trotzdem das tatsächlich verwendete Modell fest, damit spätere Läufe nachvollziehbar bleiben. Belasse die Umsetzung zunächst in deiner Opus-Hauptsession; ein zusätzlicher Worker ist für diesen Versuch unnötig.

## Formuliere eine überprüfbare Übergabe

Für eine beispielhafte zusätzliche Exportspalte könntest du den Recherche-Agent so beauftragen:

> Nutze Explore, um den bestehenden CSV-Export zu untersuchen. Finde Spaltendefinition, Datenzuordnung und zugehörige Tests. Erkläre die Behandlung fehlender Werte anhand konkreter Stellen. Melde Unsicherheiten. Begrenze dich auf die Untersuchung; die Hauptsession übernimmt Planung und Umsetzung.

Als Ergebnis reicht eine kurze Übersicht mit Datei und Zeile, der zuständigen Funktion, vorhandenen Tests und offenen Fragen. Ein langer Bericht über die gesamte Anwendung würde die anschließende Integration erschweren.

Die Hauptsession prüft besonders die Stellen, von denen eine Entscheidung abhängt. Wenn der Recherche-Agent behauptet, fehlende Werte würden als leere Zeichenfolge ausgegeben, sollte er die entsprechende Zuordnung zeigen. Fehlt sie, muss die Untersuchung weitergehen. Eine plausible Zusammenfassung ersetzt diese Kontrolle kaum.

Weitere Rollenformulierungen findest du in den [Rollen-Prompts für Claude Code und Codex](post:rollen-prompts-fuer-claude-code-und-codex). Für diesen Versuch ist die nützliche Ergänzung eine feste Ergebnisform, an der du eine gelungene Übergabe erkennst.

## Vergleiche ganze Aufgaben

Ein günstigerer Rechercheaufruf kann attraktiv aussehen und später zusätzliche Arbeit verursachen. Deshalb schlage ich folgenden Vergleich vor. Er ist ein Prüfverfahren für dein Projekt, kein bereits durchgeführter Test.

Wähle mehrere abgeschlossene, repräsentative Aufgaben, deren Ausgangszustand du wiederherstellen kannst. Verwende je Aufgabe dieselbe Anforderung, dieselben Dateien und dieselben Abnahmekriterien. Lass einmal Opus die gesamte Arbeit erledigen. Im zweiten Durchlauf recherchiert Haiku, während Opus anschließend integriert und umsetzt. Die Läufe erhalten jeweils einen frischen Arbeitskontext und Zugriff auf denselben Projektstand.

Lege die Bewertung vorab fest:

| Kriterium | Was du erfasst |
|---|---|
| Gesamter Modellverbrauch | Eingabe-, Ausgabe- und verfügbare Cache-Tokens aller Agents und der Hauptsession |
| Gesamtkosten | Gesamte abgerechnete Modellnutzung einschließlich erneuter Recherche, Review und Korrekturen |
| Nacharbeit | Falsche Fundstellen, ausgelassene Anforderungen und nötige Korrekturschleifen |
| Tests | Dieselben passenden Prüfungen und ihre Ergebnisse für beide Varianten |
| Ergebnisqualität | Erfüllte Anforderungen, korrekte Randfälle und überprüfbare Rechercheaussagen |
| Integration | Aufwand zum Kontrollieren, Zusammenführen und Nachfordern der Ergebnisse |

Bewerte die fertigen Änderungen möglichst ohne sichtbare Modellnamen. Wechsle die Reihenfolge der Varianten zwischen Aufgaben. Wiederholte Läufe helfen dir, schwankende Ergebnisse zu erkennen. Wenn deine Oberfläche keine vollständigen Verbrauchsdaten liefert, halte diese Lücke fest; aus einem günstigeren Teilaufruf lässt sich dann keine Gesamtersparnis ableiten.

## Wann die Aufteilung mehr Aufwand erzeugt

Eine winzige Textänderung braucht selten einen eigenen Recherche-Agent. Auch eng gekoppelte Entscheidungen lassen sich schwer übergeben: Wenn jede Antwort sofort eine neue Architekturfrage auslöst, wächst der Abstimmungsaufwand. Starte deshalb mit einem Recherchepaket und erweitere erst nach einem brauchbaren Vergleich.

Mehrere gleichzeitig recherchierende Agents können dieselben Dateien mehrfach lesen. Sie benötigen jeweils Kontext, und die Hauptsession muss ihre Ergebnisse prüfen. Plane parallele Aufträge nur für unabhängige Fragen mit klaren Grenzen. Code-Recherche und die Untersuchung einer getrennten Schnittstelle wären ein möglicher Versuch.

Vox verweist zur Motivation auf eine Demo mit Managed Agents. Deren Kosten und Laufzeiten beschreiben einen anderen Aufbau und eine andere Aufgabe. Daraus lässt sich kein entsprechender Vorteil für deinen Coding-Ablauf ableiten.{q:1}

Teste die Aufteilung als Nächstes an einer kleinen, realistischen Rechercheaufgabe. Wenn die Fundstellen stimmen, die Übergabe kurz bleibt und die Gesamtbewertung passt, kannst du weitere Aufgaben hinzufügen. Wenn Opus die Recherche weitgehend wiederholen muss, grenze zuerst den Auftrag genauer ein oder lasse diese Aufgabenklasse beim Hauptmodell.
