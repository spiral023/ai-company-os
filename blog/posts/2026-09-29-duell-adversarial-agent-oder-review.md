---
titel: "Adversarial Agent statt menschlichem Review? Die These ist plausibel, aber ungeprüft"
datum: 2026-09-29
kategorie: duell
zusammenfassung: "Boris Tane will den Code Review durch einen zweiten Agenten ersetzen, die Praxis-Quellen halten den Menschen als letztes Gate. Was die Positionen trennt, wie dünn beide belegt sind und was ein Team daraus machen sollte."
status: entwurf
quellen:
  - 2026-02-20-boris-tane-sdlc-is-dead
  - 2026-09-27-anthropic-academy-sdlc-playbook
  - 2026-02-23-elvis-openclaw-codex-agent-swarm
  - 2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein
  - 2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck
---

## Kurz gesagt

- Position A (Boris Tane): Code Review ist der Flaschenhals im Agent-Zeitalter, ein zweiter Adversarial Agent soll ihn ersetzen. Belegt ist das nur als Meinung, ohne Daten.
- Position B (Review-Gate): Der Agent liefert ausschließlich Pull Requests, ein Mensch gibt frei. Auch das ist überwiegend Meinung und Herstellerleitfaden, aber breiter und von mehreren unabhängigen Stimmen getragen.
- Die Positionen unterscheiden sich weniger im Werkzeug als in der Frage, wer am Ende haftet. Praktisch sind sie näher beieinander, als der Titel des Duells vermuten lässt: Auch Position B setzt Agent-Reviewer ein, nur vor dem Menschen statt an seiner Stelle.
- Empfehlung: Adversarial Reviewer einführen, menschliche Freigabe risikobasiert verschlanken, aber nicht abschaffen.

## Position A: Der Agent prüft den Agenten

Tane argumentiert, dass mit Coding-Agents die klassischen SDLC-Phasen zu einem engen Loop aus Intent, Build und Observe verschmelzen. Der Code Review gilt darin als Flaschenhals, den ein zweiter, gegnerisch angelegter Agent ersetzen soll. Sicherheitsnetz wäre Monitoring in Produktion, dessen Telemetrie zurück in den Kontext des Agenten fließt.

Wichtig für die Belegstärke: Die Wissensbasis stützt sich hier nicht auf Tanes Original, sondern auf eine deutsche Aufarbeitung (vibedeck), also eine Sekundärquelle. Die Notiz selbst nennt den Artikel eine reine Position ohne Daten und den Ersatz menschlichen Reviews „nicht belegt“. Der Closed Loop ist plausibel, wird aber nicht gezeigt.

## Position B: Der Agent schreibt, der Mensch gibt frei

Das Muster CI-Agent mit Review-Gate (Konfidenz: mehrfach-belegt) lässt den Agenten event-getriggert in einer Sandbox laufen und sein Ergebnis nur als Merge Request oder Pull Request zurückspielen. Der Reviewer-Schritt ist identisch mit dem Team-Review für menschliche Beiträge. Anthropics Playbook vom 27. September formuliert es strikt: Der schreibende Agent genehmigt nicht selbst, Agenten-Befunde blockieren keinen PR, die Code-Owner-Freigabe bleibt.

Dazu kommt das Muster Plan-first mit getrenntem Review (Konfidenz: verifiziert). Es trennt Builder, Reviewer und Verifier und eskaliert die Prüfung stufenweise bis zur modellübergreifenden Schleife. Wichtig: Dieses Muster liefert die Mechanik für Tanes Adversarial Agent, nicht das Argument gegen ihn. Es geht um den frischen Blick auf den Plan oder Diff, nicht um die Frage, ob am Ende ein Mensch unterschreibt. Und die Konfidenz „verifiziert“ bezeichnet die Stimmigkeit des Musters in der Wissensbasis; die Einzelbelege darunter sind fast alle als Meinung eingestuft.

## Wo sich die Positionen wirklich unterscheiden

| Aspekt | A: Adversarial Agent ersetzt Review | B: Agent-Review vor menschlichem Gate |
|---|---|---|
| Was der Review leisten soll | Fehler finden, schnell und skalierbar | Fehler finden und Verantwortung zuweisen |
| Engpass | Mensch soll aus dem Pfad | Review-Kapazität begrenzt die Parallelität |
| Risikoprofil | Fehler, die beide Agenten teilen, rutschen durch; Absicherung nur über Monitoring nach dem Deploy | Fehler werden vor dem Merge gefangen, dafür bleibt der Mensch Nadelöhr |
| Kosten | Zusätzliche Agent-Läufe, aber keine Wartezeit auf Menschen | Agent-Läufe plus menschliche Zeit; laut Elvis 5 bis 10 Minuten pro PR (Selbstbericht) |
| Voraussetzung | Gute Observability, schnelles Rollback | Belastbarer Team-Review-Prozess |

Der Kern ist die Aufgabe des Reviews. Für Tane ist Review Qualitätssicherung, und die lässt sich delegieren. Für das Gate ist Review auch ein Freigabeakt: Jemand aus dem Team steht dafür ein. Ein Agent kann Befunde liefern, aber keine Verantwortung tragen. Der Playbook-Satz „der Autor genehmigt nicht selbst“ ist ein Organisationsprinzip und keine Aussage über die Trefferquote von Agenten.

Beim Risikoprofil hilft ein Gedanke aus Matt Pococks Vortrag zum PR-Bottleneck: Die Review-Tiefe richtet sich danach, ob eine Entscheidung schwer umkehrbar ist und wie groß der Blast Radius ist. Ein Tippfehler im Changelog braucht keinen Menschen, eine Migration auf der Produktionsdatenbank schon. Das ist ein Praxisbericht eines Einzelnen ohne Messdaten, aber er löst den Gegensatz auf: Die Frage lautet nicht „Agent oder Mensch“, sondern „für welche Änderungen“.

## Wie belastbar ist jede Seite?

- **A:** Eine Sekundärquelle, reine Position, keine Daten. Die Wissensbasis vermerkt selbst, dass die These der Praxis mit Review-Gates widerspricht. Es gibt keinen Beleg, dass Agent-Review menschlichen Review in Fehlerquote oder Kosten erreicht.
- **B:** Breiter, aber ebenfalls ohne Messung. Herstellerdoku und Playbook beschreiben ein Vorgehen ohne Wirkungszahlen. Das GitHub-Actions-Muster stammt aus einem Betriebsbericht, bleibt aber Sekundärquelle. Elvis' Setup mit drei AI-Reviewern vor dem Menschen ist ein Selbstbericht; seine Modellurteile (Codex mit wenigen False Positives, Claude Code eher bestätigend) sind ungeprüft.
- **Die einzige Zahl:** Ein TikTok-Creator zitiert eine Auswertung von über 932.000 Pull Requests: 61,38 Prozent der KI-generierten PRs ohne dokumentierte Review, bei 58,77 Prozent der geprüften sahen nur Agenten den Code. Eine frische Prüf-Session mit der ursprünglichen Aufgabe soll die Endkorrektheit von 71,6 auf 89,7 Prozent heben. Die Studie ist nicht verlinkt, es liegt nur die Caption vor. Die Werte sind unverifizierte Zweitwiedergabe und taugen als Hinweis, nicht als Beleg. Sie stützen ohnehin nur die Trennung von Autor und Prüfer, nicht den Wegfall des Menschen.

Fazit der Belegstärke: Keine der beiden Seiten hat Messungen. B hat mehr unabhängige Stimmen, A hat die schlankere Story. Wer A umsetzt, geht auf einer Meinung ins Risiko.

## Wann welche Position trägt

**A trägt**, wenn eine Änderung leicht rückholbar ist (Feature Flag, Canary, schneller Rollback), der Blast Radius klein bleibt und Tests sowie Monitoring stark sind. Ein Warnsignal bleibt: Passt der Agent Tests an, damit sie grün werden, ist das kein Erfolg. Pocock weist zudem darauf hin, dass grüne Checks lügen können (tautologische Tests, wegmockende Tests). Ein Adversarial Agent ist nur so gut wie die Checks, auf die er sich stützt. Das prüfende Modell sollte laut der TikTok-Quelle mindestens so stark sein wie das erzeugende, was die Kosten verdoppelt (eigene Ableitung aus der Quelle, nicht gemessen).

**B trägt**, wenn Änderungen schwer umkehrbar sind, Compliance oder Audit-Pflichten gelten oder ein Fehler teuer ist. Dort braucht es eine Person, die freigibt. Die Grenze von B liegt im Team selbst: Ein oberflächliches Review lässt Agent-Fehler genauso durch wie menschliche. Ohne belastbaren Review-Prozess automatisiert das Gate nur die Zuführung ungeprüfter Änderungen.

## Empfehlung für ein Team

1. **Führe den Adversarial Agent ein, aber als Vorstufe.** Ein Reviewer mit frischem Kontext, der Diff, Plan und Originalaufgabe sieht und Lücken meldet statt Stilfragen. Das ist in beiden Lagern unstrittig.
2. **Lass den Menschen nicht aus dem Merge-Pfad, solange du keine eigenen Zahlen hast.** Miss zwei bis vier Wochen, wie viele Agent-Befunde real waren und was der Agent übersehen hat, was danach ein Mensch fand. Erst diese eigene Messung rechtfertigt, Position A für bestimmte Änderungsklassen zu übernehmen.
3. **Staffle nach Umkehrbarkeit.** Kleine, rückholbare Änderungen mit grünen Checks und Agent-Freigabe; Migrationen, Sicherheit und Datenzugriffe immer mit menschlicher Freigabe. Branch-Schutz mit Required Status Checks bleibt aktiv.
4. **Plane die Kosten ein.** Mehr Review-Läufe bedeuten mehr Tokens pro PR; beziffert hat das keine der Quellen.

Kurz: Tane hat recht damit, dass der Mensch als alleiniger Prüfer nicht mitskaliert. Belegt ist nur nicht, dass er als Freigeber verzichtbar ist.
