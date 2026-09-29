---
titel: "Adversarial Agent statt menschlichem Review? Als Vorstufe ja, als Ersatz nein"
datum: 2026-09-30
kategorie: duell
zusammenfassung: "Boris Tane will den Code Review durch einen zweiten Agenten ersetzen, die Praxis hält den Menschen als letztes Gate. Was die Positionen trennt und was ein Team daraus machen sollte."
status: freigegeben
geprueft_am: 2026-09-29
freigabe: automatisch
quellen:
  - 2026-02-20-boris-tane-sdlc-is-dead
  - 2026-09-27-anthropic-academy-sdlc-playbook
  - 2026-02-23-elvis-openclaw-codex-agent-swarm
  - 2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein
  - 2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck
---

## Kurz gesagt

- Position A (Boris Tane): Code Review ist der Flaschenhals im Agent-Zeitalter, ein zweiter Adversarial Agent soll ihn ersetzen.{q:1}
- Position B (Review-Gate): Der Agent liefert nur Pull Requests, ein Mensch gibt frei.{q:2}
- Die Positionen liegen näher beieinander, als der Titel vermuten lässt: Auch B setzt Agent-Reviewer ein, nur vor dem Menschen statt an seiner Stelle. Der Streit dreht sich darum, wer am Ende haftet.
- Setze einen Adversarial Reviewer als Vorstufe ein und schlanke die menschliche Freigabe nach Risiko ab. Abschaffen solltest du sie nicht.

## Position A: Der Agent prüft den Agenten

Tane argumentiert, dass mit Coding-Agents die klassischen SDLC-Phasen zu einem engen Loop aus Intent, Build und Observe verschmelzen. Der Code Review ist darin der Flaschenhals, den ein zweiter, gegnerisch angelegter Agent ersetzen soll. Das Sicherheitsnetz wäre Monitoring in Produktion, dessen Telemetrie zurück in den Kontext des Agenten fließt.{q:1}

Der Artikel zeigt keine Daten. Der Closed Loop klingt plausibel, wird aber nirgends vorgeführt.

## Position B: Der Agent schreibt, der Mensch gibt frei

Beim Muster „CI-Agent mit Review-Gate“ läuft der Agent event-getriggert in einer Sandbox und spielt sein Ergebnis nur als Merge Request oder Pull Request zurück. Der Review-Schritt ist derselbe wie bei menschlichen Beiträgen. Anthropics Playbook vom 27.09.2026 formuliert es strikt: Der schreibende Agent genehmigt nicht selbst, Agenten-Befunde blockieren keinen PR, die Freigabe durch die Code-Owner bleibt.{q:2}

Dazu kommt „Plan-first mit getrenntem Review“. Es trennt Builder, Reviewer und Verifier und eskaliert die Prüfung stufenweise bis zur modellübergreifenden Schleife. Das liefert die Mechanik für Tanes Adversarial Agent, nicht das Argument gegen ihn. Es geht um den frischen Blick auf Plan oder Diff, nicht darum, ob am Ende ein Mensch unterschreibt.{q:2}

## Wo sich die Positionen wirklich unterscheiden

| Aspekt | A: Adversarial Agent ersetzt Review | B: Agent-Review vor menschlichem Gate |
|---|---|---|
| Was der Review leisten soll | Fehler finden, schnell und skalierbar | Fehler finden und Verantwortung zuweisen |
| Engpass | Der Mensch soll aus dem Pfad | Review-Kapazität begrenzt die Parallelität |
| Risiko | Fehler, die beide Agenten teilen, rutschen durch. Absicherung nur über Monitoring nach dem Deploy | Fehler werden vor dem Merge gefangen, der Mensch bleibt Nadelöhr |
| Kosten | Zusätzliche Agent-Läufe, keine Wartezeit auf Menschen | Agent-Läufe plus menschliche Zeit, laut Elvis 5 bis 10 Minuten pro PR{q:3} |
| Voraussetzung | Gute Observability, schnelles Rollback | Belastbarer Team-Review-Prozess |

Der Kern ist die Aufgabe des Reviews. Für Tane ist er Qualitätssicherung, und die lässt sich delegieren. Für das Gate ist er auch ein Freigabeakt: Jemand aus dem Team steht dafür ein. Ein Agent liefert Befunde, aber trägt keine Verantwortung. „Der Autor genehmigt nicht selbst“ ist ein Organisationsprinzip und sagt nichts über die Trefferquote von Agenten.

Matt Pococks Vortrag zum PR-Bottleneck löst den Gegensatz auf.{q:5} Die Review-Tiefe richtet sich danach, wie schwer eine Entscheidung umkehrbar ist und wie groß der Blast Radius. Ein Tippfehler im Changelog braucht keinen Menschen, eine Migration auf der Produktionsdatenbank schon. Die Frage lautet also nicht „Agent oder Mensch“, sondern „für welche Änderungen“.

## Was die Zahlen hergeben

Keine Seite hat Messungen, die den Ersatz oder Nicht-Ersatz des Menschen belegen. Die einzige Zahl kommt von einem TikTok-Creator, der eine Auswertung von über 932.000 Pull Requests zitiert: 61,38 Prozent der KI-generierten PRs hatten keinen dokumentierten Review, bei 58,77 Prozent der geprüften sahen nur Agenten den Code. Eine frische Prüf-Session mit der ursprünglichen Aufgabe soll die Endkorrektheit von 71,6 auf 89,7 Prozent heben.{q:4} Die Studie ist nicht verlinkt, du kannst die Zahlen also nur als Hinweis nehmen. Sie stützen ohnehin nur die Trennung von Autor und Prüfer, nicht den Wegfall des Menschen.

Elvis setzt drei AI-Reviewer vor den Menschen.{q:3} Seine Einschätzung, Codex melde wenige False Positives und Claude Code bestätige eher, ist eine Einzelbeobachtung.

## Wann welche Position trägt

**A trägt**, wenn eine Änderung leicht rückholbar ist (Feature Flag, Canary, schneller Rollback), der Blast Radius klein bleibt und Tests sowie Monitoring stark sind. Ein Warnsignal ist, wenn der Agent Tests anpasst, damit sie grün werden. Pocock weist darauf hin, dass grüne Checks lügen können, etwa durch tautologische oder wegmockende Tests.{q:5} Ein Adversarial Agent ist nur so gut wie die Checks, auf die er sich stützt. Das prüfende Modell sollte laut TikTok-Quelle mindestens so stark sein wie das erzeugende. Das verdoppelt grob die Kosten (eigene Ableitung, nicht gemessen).{q:4}

**B trägt**, wenn Änderungen schwer umkehrbar sind, Compliance oder Audit-Pflichten gelten oder ein Fehler teuer ist. Dort braucht es eine Person, die freigibt. Die Grenze von B liegt im Team: Ein oberflächlicher Review lässt Agent-Fehler genauso durch wie menschliche. Ohne belastbaren Review-Prozess automatisiert das Gate nur die Zuführung ungeprüfter Änderungen.

## Empfehlung für ein Team

1. **Führe den Adversarial Agent als Vorstufe ein.** Ein Reviewer mit frischem Kontext, der Diff, Plan und Originalaufgabe sieht und Lücken meldet statt Stilfragen. Das ist in beiden Lagern unstrittig.
2. **Lass den Menschen im Merge-Pfad, bis du eigene Zahlen hast.** Miss zwei bis vier Wochen, wie viele Agent-Befunde real waren und was danach ein Mensch fand, das der Agent übersehen hatte. Erst diese Messung rechtfertigt, A für bestimmte Änderungsklassen zu übernehmen.
3. **Staffle nach Umkehrbarkeit.** Kleine, rückholbare Änderungen mit grünen Checks und Agent-Freigabe. Migrationen, Sicherheit und Datenzugriffe immer mit menschlicher Freigabe. Branch-Schutz mit Required Status Checks bleibt aktiv.
4. **Plane die Kosten ein.** Mehr Review-Läufe bedeuten mehr Tokens pro PR. Beziffert hat das bisher keine Quelle.
