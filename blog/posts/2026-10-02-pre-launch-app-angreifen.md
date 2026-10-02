---
titel: "Vor dem Launch: Lass Agenten deine App angreifen"
datum: 2026-10-02
kategorie: arbeitsweisen
zusammenfassung: "Vier read-only Prüfagenten greifen deine vibe-coded App vor dem Release in einer Testumgebung an. Ablauf, 16 Prüffragen, Schutzrahmen und die Grenzen des Verfahrens."
status: freigegeben
geprueft_am: 2026-10-02
quellen:
  - 2026-09-27-voxyz_ai-2104224555040452925
  - 2026-09-26-voxyz_ai-2103977414711767244
  - 2026-09-29-suraj_sharma14-2104790775397830755
---

## Kurz gesagt

- Vor dem ersten Release lässt du vier Prüfagenten mit festem Fragenkatalog versuchen, deine App zu brechen: Security, Daten, Abläufe, Umgebung.{q:1}
- Die Agenten dürfen nur lesen, Befehle ausführen und einen Browser bedienen. Behoben wird erst, nachdem du die Befundliste gesehen hast.{q:1}
- Arbeite ausschließlich in einer Testumgebung mit Testkonten, Payment-Testmodus und Test-Datenbank.
- Erweitere den Katalog um Punkte, die er auslässt, etwa Row Level Security, CORS und Ausgabenlimits.{q:3}

## Das Problem

Wer mit einem Coding Agent schnell eine App baut, prüft selten, was passiert, wenn jemand die Oberfläche umgeht. Der Agent liefert Funktionen, die im Happy Path laufen. Ob der Server eine fremde ID akzeptiert oder ein Preis im Request änderbar ist, fragt niemand, solange es nicht schiefgeht.

Vox (@Voxyz_ai auf X) schlägt dafür einen festen Schritt vor dem Launch vor: Ein Agent behebt, vier andere haben nur die Aufgabe, die App zu brechen.{q:1} Das ist ein Praxistipp mit Fragenliste ohne Messung, als Arbeitsvorlage taugt er trotzdem.

## Der Ablauf

1. **Prüfer anlegen.** Vier Subagents mit je einem Themenbereich: `security-breaker`, `data-breaker`, `flow-breaker`, `env-breaker`. Sie bekommen Leserechte, dürfen Befehle ausführen und per Playwright den Browser steuern. Code und Konfiguration dürfen sie nicht ändern.{q:1}
2. **Dateien erst zeigen lassen.** Der Hauptagent legt die Agent-Dateien erst an, nachdem du sie gesehen und bestätigt hast.{q:1}
3. **Testumgebung vorbereiten.** Zwei Testkonten, Payment im Testmodus, Test-Datenbank (siehe unten).
4. **Katalog abarbeiten.** Jeder Prüfer geht seine Fragen Punkt für Punkt durch. Was sich nicht prüfen lässt, markiert er mit Grund als „untested“.{q:1}
5. **Befunde bündeln.** Jeder Befund kommt mit Repro-Schritten, Screenshot und Fix-Vorschlag, sortiert nach Schwere.{q:1}
6. **Beheben.** Erst nach deiner Freigabe arbeitet die Hauptsession die Liste ab. Ein einziger Agent schreibt, damit nicht zwei Agenten dieselbe Datei ändern.{q:2}

Bei der Effort-Stufe trennt Vox: Alle vier laufen auf `high`, der Security-Prüfer auf `xhigh` oder `max`, weil dort Login und Zahlung liegen. Mehr Effort kaufe laut Post vor allem mehr Verifikation und Randfalltests.{q:1} Ob das die Befundquote verbessert, zeigt der Post nicht.

## Die 16 Fragen

| Bereich | Was der Prüfer versucht |
|---|---|
| Security | Private Schlüssel (`sk_`, `service_role`) im Frontend-Bundle oder in der Git-Historie suchen. API direkt aufrufen, ausgeloggt oder mit fremder ID. Preis, Menge oder Rolle im Request ändern. Denselben Endpunkt 100-mal hintereinander aufrufen (Rate Limit pro User und IP?). Script-Snippet in Markdown, Rich Text oder SVG verstecken und prüfen, ob es bei einem anderen Konto läuft.{q:1} |
| Daten | 10.000 Datensätze laden. 200 Zeichen langer Name mit Emoji. Dieselbe E-Mail in anderer Groß- und Kleinschreibung registrieren. Leeres Formular absenden und prüfen, ob ein leerer Datensatz entsteht.{q:1} |
| Abläufe | Dieselbe Bestellung zweimal gleichzeitig auslösen und denselben Payment-Webhook zweimal abspielen. Neu laden oder Zurück mitten im Formular. Offline speichern, während die App „gespeichert“ meldet. 50-MB-Upload.{q:1} |
| Umgebung | Kleines Handy bei 200 % Zoom. Safari-Engine. Andere Zeitzonen, in denen Daten und Fristen um einen Tag verrutschen.{q:1} |

Die Fragen sind knapp formuliert und lassen sich ohne Vorwissen als Prüfauftrag nutzen. Eine frühere Fassung desselben Autors deckte andere Bereiche ab: Design-Konsistenz, Mobile, alle UI-Zustände, Nutzung wie ein echter User und Launch-Basics, zusammen 20 Punkte mit fünf Subagents.{q:2} Je nach App-Typ wählst du den einen oder den anderen Katalog, oder du kombinierst beide.

## Die Testumgebung

Die Prüfer sollen wirklich angreifen, deshalb darf nichts Echtes in Reichweite sein.{q:1}

- **Login:** zwei eigene Testkonten, die du bereitstellst. Der Agent fragt danach, statt selbst Konten anzulegen.
- **Zahlung:** nur im Testmodus des Zahlungsanbieters.
- **Datenbank:** Testdaten nur in eine Test-Datenbank schreiben und danach aufräumen.
- **KI-Schnittstellen:** mocken, oder einen Key mit Ausgabenlimit verwenden.
- **Stopp:** Findet der Agent Produktionsschlüssel oder eine Live-Domain, hört er sofort auf und fragt nach.

## Den Katalog erweitern

16 Fragen decken nicht alles ab. Eine 30-Punkte-Checkliste von Suraj Sharma liefert, was fehlt: Row Level Security für jede Tabelle, CORS nur auf eigene Domains, sichere Cookies, CSRF-Schutz, ablaufende Sessions, Backups mit Restore-Test.{q:3} Dazu kommen KI-spezifische Risiken wie von der KI erfundene Paketnamen, Prompt Injection und Grenzen für Tool- und SQL-Ausführung durch das Modell sowie harte Ausgabenlimits bei KI-Anbietern.{q:3} Mach aus jedem dieser Punkte eine Frage im Stil von Vox: Was tust du, und was darf nicht passieren?

## Grenzen

- Der Prüfer findet nur, wonach der Katalog fragt. Was nicht auf der Liste steht, bleibt unentdeckt.
- Wirkung und Kosten sind nicht gemessen. Wie viele Fehler das findet und was vier Opus-Agents auf hohem Effort kosten, geben die Quellen nicht an.{q:1}
- Der Schutzrahmen besteht aus Anweisungen an den Agenten. Die Regel „bei Produktionsschlüsseln stoppen“ ist keine technische Sperre. Gib deshalb gar nicht erst Zugang zu Produktionsschlüsseln, statt dich auf den Stopp zu verlassen.{q:1}
- Bei sensiblen Daten oder regulierten Bereichen ersetzt der Check kein Security-Review durch Fachleute.
- Zwei der drei Quellen stammen vom selben Autor, nur die Checkliste ist unabhängig.

## Einordnung und Empfehlung

Der Check ergänzt menschliches Code-Review, weil er jedes Mal dieselben Fragen stellt, die beim Bauen untergehen. Wie ein zweiter Agent als Vorstufe vor dem Menschen funktioniert, steht im [Duell zu Adversarial Agents und Review](post:duell-adversarial-agent-oder-review).

Richte die vier Prüfer einmal ein und starte sie vor jedem Release sowie vor größeren Änderungen an Login, Zahlung, Uploads oder Datenmodell. Erweitere den Katalog nach jedem gefundenen Fehlertyp. Verarbeitet die App Zahlungs- oder Personendaten, plane zusätzlich eine Prüfung durch Sicherheitsfachleute ein.
