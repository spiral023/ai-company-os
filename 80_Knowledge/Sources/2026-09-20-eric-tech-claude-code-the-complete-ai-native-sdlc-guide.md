---
url: https://www.youtube.com/watch?v=6CaQ9ZFuuKI
autor: Eric Tech
datum: 2026-09-20
erfasst: 2026-10-05
typ: video
rohquelle: 00_Inbox/Quellen/YouTube/2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide.md
beleg_art: sekundaerquelle
zeitkritisch: nein
---

# Intent, Prüfungen und Betriebsfeedback verbinden den AI-nativen SDLC

Eric Tech erläutert Anthropics AI-native SDLC-Playbook als durchgängigen Ablauf mit Claude Code. Wenn die Umsetzung schneller wird, müssen Anforderungsklärung, Review und Release mithalten. Das Video ist eine praktische Aufarbeitung des bereits erfassten Academy-Kurses, keine unabhängige Fallstudie zur Wirkung des Vorgehens.

## Vom Warum zum ausführbaren Plan

Der Ablauf beginnt mit einer Klärungssession, in der der Agent Fragen stellt und Entscheidungen erfasst. Eine `intent.md` hält Problem, gewünschtes Ergebnis, betroffene Nutzer, Einschränkungen und offene Fragen fest. Eric unterscheidet drei Aufgaben der Artefakte: Intent erklärt das Warum, die `spec.md` definiert Anforderungen und erwartetes Verhalten, die `plan.md` beschreibt die Umsetzung mit Dateien, Reihenfolge, Risiken und Nachweisen.

Intent muss laut Video nicht als einzige Datei für das ganze Projekt bestehen: Änderungen können eigene Intents bekommen, und ein Ticketsystem kann die führende Ablage sein. Bereits funktionierende Spec- und Plan-Workflows sollen weitergenutzt und mit dem Playbook verglichen werden. Das Video nennt Matt Pococks Skills und Superpowers als mögliche Varianten, ohne deren Wirksamkeit zu vergleichen.

## Verhalten testen und den Agent-Workflow separat evaluieren

Tests sollen vor der Implementierung einen überprüfbaren Sollzustand liefern. Ein Agent erhält eine Rückkopplung aus Tests, Linting und Build und korrigiert Fehler, bevor ein Mensch das Ergebnis prüft. Der Sprecher unterscheidet Funktions-, Komponenten- und End-to-End-Tests; die Beschreibung nennt unter anderem Jest, Vitest, React Testing Library und Playwright.

Davon getrennt stehen Evals für den Agent-Workflow: Eric übernimmt die Playbook-Empfehlung, 20 bis 50 bereits bearbeitete reale Aufgaben mit erwarteten Ergebnissen als Eval-Satz zu verwenden. Modell- oder Regeländerungen sollen gegen diese Aufgaben in CI geprüft werden. Die Zahl ist eine empfohlene Startgröße, kein Messergebnis. Ein bestandener Anwendungstest und ein erfolgreicher Agent-Eval beantworten unterschiedliche Fragen.

## Review-Regeln aus menschlichem Feedback gewinnen

Eine `REVIEW.md` beschreibt Prüfdurchgänge, relevante Befunde, Grenzen für Detailkritik und auszunehmende Dateien. Als eigene Empfehlung schlägt Eric vor, frühere PR-Kommentare von Menschen auswerten zu lassen und wiederkehrende Befunde als Kandidaten für Review-Regeln zu sammeln. Ein Tech Lead kann daraus die Team-Standards formulieren, denen der Review-Agent folgt.

Hooks ergänzen das Review um technische Grenzen für geschützte Dateien, sensible Inhalte und Aktionen wie Merge oder Deployment. Das Video beschreibt mögliche Kontrollen; es demonstriert keinen vollständigen Nachweis, dass alle kritischen Aktionen damit abgesichert sind.

## Betriebsfeedback führt zur nächsten Anforderung

Vor dem Deployment kann ein Agent fehlgeschlagene Builds untersuchen und einen Korrektur-PR zur Prüfung vorbereiten. Nach dem Deployment sollen Status- und Monitoring-Daten Fehler sichtbar machen. Der Sprecher skizziert Rollback und Ursachenanalyse mit anschließender Korrektur. Wiederkehrende Fehler, langsame Abfragen oder ungünstige Produktmetriken werden wiederum zum Ausgangspunkt einer neuen `intent.md`.

## Einordnung

Die Quelle macht bekannte Bausteine als zusammenhängenden Ablauf verständlich. Sie ergänzt den Bestand vor allem durch die Empfehlung, Review-Regeln aus früherem menschlichem PR-Feedback abzuleiten. Ein Großteil stammt aus [[2026-09-27-anthropic-academy-sdlc-playbook]] und zählt deshalb nicht als unabhängige Bestätigung dieses Playbooks.

Eine lokale Stichprobe bestätigt die genannte Plan-Variante: `external_repos/obra/superpowers/skills/writing-plans/SKILL.md` verlangt konkrete Dateien, Schnittstellen und Tests im Plan vor Codeänderungen. `external_repos/mattpocock/skills/skills/engineering/to-tickets/SKILL.md` zerlegt einen Plan oder eine Spec in vertikale Tickets mit blockierenden Abhängigkeiten. Verifiziert ist damit der Inhalt dieser Skills, nicht ihr Nutzen in einem Produktionsprojekt.

Die Auswertung basiert auf englischen automatisch erzeugten Untertiteln mit erkennbaren Erkennungsfehlern; Aussagen sind sinngemäß wiedergegeben, keine wörtlichen Zitate aus dem Transkript. Leistungszahlen, ein kontrollierter Vergleich und ein Produktionsnachweis fehlen. Evals, Tests, Review-Regeln und Monitoring verursachen laufenden Pflege- und Ausführungsaufwand. Die Rollback-Skizze erläutert die erforderliche Berechtigung und menschliche Freigabe weniger genau als das vorhandene Playbook. Daraus folgt keine pauschale Erlaubnis zu autonomen Produktionseingriffen.

## Kernaussagen

- Intent, Spec und Plan trennen Zielklärung, erwartetes Verhalten und Umsetzung; bestehende Abläufe lassen sich damit gezielt ergänzen → [[Plan-first-mit-getrenntem-Review]]
- Anwendungstests prüfen das Produkt, reale Aufgaben als CI-Evals prüfen Veränderungen am Agent-Workflow → [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]]
- Wiederkehrende menschliche PR-Kommentare können Kandidaten für Regeln in `REVIEW.md` liefern; Hooks ergänzen technisch erzwingbare Grenzen → [[CI-Agent-mit-Review-Gate]]

## Verbindungen

- [[2026-09-27-anthropic-academy-sdlc-playbook]]
- [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]]
- [[Testharness-als-staerkster-Hebel]]
- [[Thema-AI-nativer-SDLC]]
- [[Thema-Verifikation-Tests-Review]]
