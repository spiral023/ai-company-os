---
url: https://www.tiktok.com/@floknowsai/video/7673935893886979360
autor: "@floknowsai"
datum: 2026-08-14
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Agent-Review ohne Mensch: frische Prüf-Session statt Selbstkontrolle

Ein TikTok-Creator zitiert eine Auswertung der Universität Toruń von über 932.000 Pull Requests: 61,38 Prozent der KI-generierten PRs hatten keine dokumentierte Review, 58,77 Prozent der geprüften wurden nur von Agenten gesehen. Die Studie selbst ist nicht verlinkt, nur die Caption liegt vor (kein Transkript); die Zahlen sind damit unverifizierte Zweitwiedergabe.

## Kernaussagen
- Ein Agent meldet Fehler seltener, wenn sie im selben Gesprächsverlauf entstanden sind; eine frische Prüfung mit der ursprünglichen Aufgabe hebt laut Caption die Endkorrektheit von 71,6 auf 89,7 Prozent. → [[Plan-first-mit-getrenntem-Review]]
- Das prüfende Modell soll mindestens gleich stark sein wie das erzeugende. → [[CI-Agent-mit-Review-Gate]]
- Getestet wird geändertes Verhalten, nicht jede Änderung; ein Refactoring muss unter unveränderten Tests grün bleiben. Werden Tests angepasst, damit sie grün werden, ist das ein Warnsignal. → [[TDD-als-Verifikationshebel]]
- Erzwingen über Branch-Rules: `Require status checks to pass before merging`.

## Einordnung
Die Trennung von Erzeuger- und Prüfkontext ist plausibel und passt zum Bestand, die konkreten Prozentwerte sind aber ungeprüft. Kosten: zusätzlicher Review-Lauf mit mindestens gleich teurem Modell.

## Verbindungen
- [[Plan-first-mit-getrenntem-Review]]
- [[CI-Agent-mit-Review-Gate]]
- [[Testharness-als-staerkster-Hebel]]
