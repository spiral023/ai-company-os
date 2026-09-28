---
url: https://www.tiktok.com/@promptgefluester/video/7666715032855661857
autor: "@promptgefluester"
datum: 2026-07-26
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Warum professionelles AI-Coding langsam ist: Quality Gates statt Vibe-Coding-Illusion

Ein Praktiker mit eigenem, über Monate gebautem „Code Guard“ argumentiert, dass die Geschwindigkeits-Illusion von Coding Agents bei größeren Codebasen nicht trägt: Ohne dichte Gates entstehen ständig Fehler, mit Gates dauert selbst eine kleine Änderung eine halbe bis ganze Stunde. Die Belastbarkeit ist die einer Selbstauskunft aus einem Projekt; Zahlen zu Fehlerraten gibt es nicht.

## Die These: Kontrolle wird nicht geliefert, sondern erarbeitet

Der Sprecher sagt, LLMs schafften keine Kontrolle, sie entkoppelten den Entwickler davon. Sein Quality Gate korrigiere bei fast jeder Ausgabe, entferne „AI Slop“, vereinfache Code und behebe Fehler. Vor dem Deployment läuft nochmals ein Testdurchlauf, der weitere Fehler findet. Das gelte auch bei den größten Modellen: Er plant mit Fable Five und setzt mit Opus 5 um, hat aber trotzdem laufend Qualitätsprobleme.

## Was das Gate enthält

- Viele deterministische, statische Codeanalysen, die dauerhaft Fehler melden.
- Vorab-Validierung der Business-Logik und nachgelagerte Impact-Analysen.
- Erkennung von Business-Logik-Drift: Passt sich die Logik an, muss die Dokumentation fortgeschrieben und müssen Unit- und Business-Logik-Tests mit angepasst werden.
- Als Schwelle nennt er Anwendungen ab etwa 10.000 bis 20.000 Zeilen Code mit komplexer Business-Logik.

## Der Preis

Eine kleine Änderung in einer Maske braucht rund eine halbe Stunde bis zum Durchlauf; die Ergebnisse kommen nach 30 bis 60 Minuten. Dennoch baue er mehrere 100.000 Zeilen Code samt umfangreicher Business-Logik in wenigen Tagen. Er hält den Ansatz für unspaßig und vermutet, 99 Prozent der Leute würden ihn nicht wollen.

## Spekulation über die Anbieter

Er vermutet, KI-Firmen bauten solche Gates absichtlich nicht ein, um die Illusion eines fehlerfrei programmierenden Systems zu wahren. Das ist Vermutung ohne Beleg.

## Einordnung

Belastbar ist die Grundrichtung: Deterministische Prüfungen, Tests und Drift-Kontrolle als eigentlicher Hebel decken sich mit dem Bestand. Selbstberichtet sind die Zeitangaben und die Aussage, das Gate finde bei fast jeder Ausgabe Fehler; es fehlen Messwerte und ein Vergleich ohne Gate. Die Unterstellung, Anbieter ließen Gates absichtlich weg, ist unbelegt; plausibler sind Latenz-, Kosten- und Generalisierungsgründe, die die Quelle nicht nennt. Die Kosten der Arbeitsweise (Wartezeit, Pflege der Gates, Doku-Fortschreibung) werden offen benannt, Token-Kosten nicht.

## Kernaussagen

- Bei größeren Codebasen liefern deterministische Prüfungen und Tests die eigentliche Qualität, nicht das Modell allein → [[Testharness-als-staerkster-Hebel]]
- Planung mit dem stärksten Modell, Umsetzung mit dem nächstkleineren → [[Modell-Eskalation-von-guenstig-nach-teuer]]
- Geschäftslogik-Drift erfordert Impact-Analysen und fortgeschriebene Doku und Tests → [[Plan-first-mit-getrenntem-Review]]

## Verbindungen

- [[Testharness-als-staerkster-Hebel]]
- [[Plan-first-mit-getrenntem-Review]]
- [[2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5]]
- [[2026-08-21-promptgefluester-wie-macht-man-refactering-bei-einer-richtig-grossen-code-base-mit-aeh]]
- [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]]
