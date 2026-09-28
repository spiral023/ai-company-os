---
url: https://www.tiktok.com/@floknowsai/video/7668380261251419424
autor: "@floknowsai"
datum: 2026-07-30
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-07-30-floknowsai-ki-gibt-dir-das-gefuehl-dass-du-so-schnell-wie-noch-nie-arbeitest.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Gefühlte Geschwindigkeit mit KI: Warum Kontext über Treffsicherheit entscheidet

Florian Schünemann fasst in einem 96-Sekunden-Video zwei arXiv-Studien zusammen (`2507.09089`, `2602.08316`, nur als Links in der Caption): Erfahrene Entwickler arbeiten mit KI subjektiv schneller, messen aber langsamer, und die Qualität des mitgegebenen Kontexts bestimmt die Erfolgsrate. Die Zahlen stammen aus der Caption, die Studien selbst wurden nicht geprüft. Das Transkript ist eine maschinelle Rückübersetzung ins Englische und daher nur bedingt zitierfähig.

## Wahrnehmung gegen Messung

Die erste Studie (16 erfahrene Entwickler, Arbeit im eigenen Projekt, laut Transkript von der Organisation METR) hat nachgemessen. Zwölf der sechzehn wurden langsamer. Vorher erwarteten sie 24 Prozent Beschleunigung, hinterher fühlten sie noch 20 Prozent, gemessen waren es 19 Prozent mehr Zeit. Am stärksten fiel der Effekt in Projekten aus, die sie am besten kannten. Florians Erklärung: Fünf Jahre Projektwissen stecken im Kopf und kommen beim Agent nicht an. Das ist seine Deutung, keine Aussage der Zahlen.

## Kontext: richtig hilft, falsch schadet

Die zweite Studie betrifft die Erfolgsrate mit Kontext. Richtige Information hebt sie von 26 auf 34 Prozent, falsche senkt sie auf 22 Prozent, also unter den Wert ganz ohne Kontext. Die Bezugsgröße (Aufgabentyp, Modell, Stichprobe) nennt die Quelle nicht.

## Drei Stellen, an denen du Kontext steuerst

- Regeln in `CLAUDE.md`: das Briefing, etwa „nach jeder Änderung einen Test ausführen“.
- Skills in `.claude/skills/<name>/SKILL.md`: zusätzliche Fähigkeiten, etwa wie Mails formuliert werden sollen.
- Ein Wissenssystem oder Connectors: Projektwissen an einem Ort, den der Agent bei Bedarf nachschlägt.

In langen Sessions gehen Regeln im Kontext unter. Laut Florian empfiehlt Anthropic inzwischen, überflüssige Beschreibungen aus Regeldateien zu löschen (ohne Beleg im Video). Seine Schlussfolgerung: Es gibt keine allgemeine Lösung, du musst die Arbeitsumgebung pro Projekt einrichten und pflegen, und KI macht dich dort produktiver, wo du dich am besten auskennst.

## Einordnung

Die Wahrnehmungslücke (gefühlt +20 %, gemessen +19 % Zeit) ist der belastbare Kern, sofern die Zahlen aus der Studie stimmen. Die Stichprobe ist klein, bezieht sich auf erfahrene Entwickler in vertrauten Projekten und auf einen früheren Modellstand. Sie sagt wenig über Neulinge oder neue Tools. Die Kontext-Zahlen sind kontextlos zitiert und ohne Studienprüfung nicht bewertbar. Praktisch relevant ist der Hinweis, dass falscher Kontext schlechter ist als keiner, also Pflege und Löschen wichtiger sind als Sammeln. Die Sekundärverdichtung im Kurzvideo ersetzt nicht die Primärquelle.

## Kernaussagen

- Gefühlte Beschleunigung durch KI kann der Messung widersprechen; verlass dich nicht auf dein Gefühl → [[Testharness-als-staerkster-Hebel]]
- Falscher Kontext senkt die Erfolgsrate unter den Wert ohne Kontext; Regeldateien schlank und aktuell halten → [[AGENTS-md-Onboarding-Design]]
- Kontext gehört an drei Stellen: Regeln, Skills, Wissenssystem → [[Erweiterungs-Ebenen-Zuordnung]]

## Verbindungen

- [[Erweiterungs-Ebenen-Zuordnung]]
- [[AGENTS-md-Onboarding-Design]]
- [[2026-02-26-omarsar0-agents-md-evaluation]]
- [[2026-02-01-humanlayer-writing-a-good-claude-md]]
