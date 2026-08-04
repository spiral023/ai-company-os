---
url: https://x.com/Meer_AIIT/status/2027509711722188976
autor: "@Meer_AIIT (Meer | AI Tools & News)"
datum: 2026-02-27
erfasst: 2026-08-05
typ: tweet
rohquelle: 00_Inbox/Quellen/2026-02-27-meer-ai-tools-news-claude-code-best-practices-2026.md
beleg_art: sekundaerquelle
---

# Claude-Code-Power-Tipps: Was über die offizielle Doku hinausgeht

Ein Thread von @Meer_AIIT verspricht im Titel „100x Powerful“ — reine Marketingsprache, die bei der Einordnung ignoriert wird. Inhaltlich kombiniert der Thread laut eigener Angabe offizielle Anthropic-Best-Practices mit Tipps, die Boris Cherny (Claude-Code-Entwickler bei Anthropic) zugeschrieben werden. Der Abgleich mit der parallel verarbeiteten Primärquelle [[2026-08-04-anthropic-docs-claude-code-best-practices]] zeigt: Elf der dreizehn Punkte (Context Window als knappste Ressource, Self-Verification mit Testfällen im Prompt, Plan Mode/Explore-Plan-Implement, präzise statt vage Prompts, CLAUDE.md kurz halten, parallele Sessions, Subagents, Skills für Wiederholaufgaben, rohe Fehlerdaten statt Interpretation, `/clear`/`/compact`, Checkpoints/Undo) sind inhaltlich deckungsgleich mit der offiziellen Dokumentation. Diese Punkte werden hier nicht erneut ausgeführt, sondern nur verlinkt.

## Was tatsächlich zusätzlich beigetragen wird

Zwei Punkte finden sich nicht in der offiziellen Doku und sind damit die eigentliche Erkenntnis dieser Quelle:

**Voice Dictation für reichhaltigere Prompts.** Getippte Prompts sind laut Thread kurz und lassen Kontext weg, weil Tippen langsam ist; beim Sprechen liefert man nebenbei mehr Details, Hintergründe und Constraints. Boris' Team soll Voice Dictation (z. B. per Doppelklick auf die Funktionstaste am Mac) für fast alle komplexen Prompts nutzen, mit deutlich besseren Ergebnissen durch den zusätzlichen beiläufig gelieferten Kontext.

**Zwei-Claude-Review des Plans, nicht nur des Diffs.** Boris Cherny berichtet laut Thread, sein Team lasse für jede komplexe Aufgabe eine Claude-Instanz den Plan schreiben und eine zweite Instanz — in der Rolle eines Senior Engineers — diesen Plan prüfen, bevor implementiert wird. Das ist eine Nuance gegenüber dem in [[Plan-first-mit-getrenntem-Review]] und der Primärquelle beschriebenen adversarialen Review, das dort auf den fertigen Diff gegen `PLAN.md` angewendet wird: hier findet die zweite Meinung schon vor der Umsetzung statt, auf der Planebene selbst.

## Einordnung

Beide Zusatzpunkte sind Erfahrungsberichte, keine Messungen — die Zuschreibung an Boris Cherny läuft über die Sekundärfassung eines Tweet-Threads, nicht über eine geprüfte Primäraussage; die Aussage könnte paraphrasiert oder verkürzt sein. „100x Powerful“ im Titel ist ein unbelegter Marketing-Superlativ und wird nicht als Kennzahl übernommen. Die Voice-Dictation-Empfehlung ist zudem plattform- und geräteabhängig (Mac-spezifische Bedienung) und bislang nur einfach belegt. Da die übrigen elf Punkte bereits durch die Primärquelle abgedeckt sind, bleibt als eigenständiger Wert dieser Notiz nur der Verweis auf diese zwei Praktiken.

## Kernaussagen

- Voice Dictation statt Tippen liefert laut Erfahrungsbericht reichhaltigere, kontextreichere Prompts, weil Sprechen beiläufig mehr Details transportiert als Tippen → [[Voice-Prompting-fuer-Kontextreichtum]]
- Boris Chernys Team lässt eine zweite Claude-Instanz explizit den Plan (nicht nur den späteren Diff) vor der Umsetzung als Senior-Engineer-Rolle prüfen → [[Plan-first-mit-getrenntem-Review]]
- Elf von dreizehn Tipps sind deckungsgleich mit der offiziellen Anthropic-Dokumentation und werden dort ausführlich belegt → [[2026-08-04-anthropic-docs-claude-code-best-practices]]

## Verbindungen

- [[2026-08-04-anthropic-docs-claude-code-best-practices]]
- [[Plan-first-mit-getrenntem-Review]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[Voice-Prompting-fuer-Kontextreichtum]]
