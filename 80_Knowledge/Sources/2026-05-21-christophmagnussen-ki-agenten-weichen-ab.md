---
url: https://www.tiktok.com/@christophmagnussen/video/7642335774192569632
autor: "@christophmagnussen"
datum: 2026-05-21
erfasst: 2026-08-31
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-05-21-christophmagnussen-ki-agenten-weichen-ab.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Agent Drift: Warum Transparenz allein das Abdriften von Agents nicht verhindert

Christoph Magnussen beschreibt in einem 100-Sekunden-Statement (automatisches Transkript) Agent Drift als größte offene Schwierigkeit bei Multi-Agent-Systemen. Es ist eine Meinungsäußerung ohne Messung, Beispiel oder Methode; belastbar ist nur die Problembeschreibung, nicht die Lösungsansicht.

## Das Problem

Ein Agent bekommt eine Aufgabe und verliert, ohne dass es jemand bemerkt, schrittweise das Alignment zum ursprünglichen Ziel. Als Treiber nennt er das Starten von Subagents und Tools. Das Abdriften lässt sich schwer sichtbar machen: Die Denkschritte von Reasoning-Modellen sind laut ihm teils unbrauchbar, er verweist auf abstruse Beispiele aus dem ChatGPT-Thinking-Modus. Folge kann sein, dass viel Geld ausgegeben wird, weil ein Agent in die falsche Richtung gesteuert wurde. Das sei bei OpenClaw häufig passiert.

## Sichtbarkeit reicht nicht

Seine zentrale These: Die Lösung ist nicht, den Drift nur anzuzeigen, sondern an der richtigen Stelle dafür zu sorgen, dass er gar nicht erst entsteht. Das sei noch nicht richtig adressiert.

## Policies in Agent-Hierarchien

Bei Hierarchien (CEO-Agent, Fachagenten) stellt sich die Frage, was passiert, wenn ein Fachexperte widerspricht und der Rest trotzdem weitermacht. Die Entscheidungsregeln dafür (Policies) legt man entweder am Anfang fest oder überlässt sie dem Modell und liefert sich damit dessen Urteil aus. Ein „Agent-Betriebssystem“ sieht er erst auf dem Weg, nicht als erreicht.

## Einordnung

Die Quelle benennt ein reales, im Bestand bereits als Advisor-Muster geführtes Problem, liefert aber keine Lösung: Die Forderung nach Prävention „an der richtigen Stelle“ bleibt ohne Mechanismus. Die Behauptung zu OpenClaw ist ungeprüft. Nützlich ist die Unterscheidung zwischen Beobachtbarkeit und Prävention sowie der Hinweis, dass Eskalations- und Widerspruchsregeln in Multi-Agent-Hierarchien vorab definiert werden sollten, statt sie dem Modell zu überlassen. Kosten dieses Ansatzes: Vorab-Policies erhöhen den Designaufwand und begrenzen die Autonomie.

## Kernaussagen

- Agent Drift entsteht unbemerkt durch Subagent- und Tool-Aufrufe und ist schwer transparent zu machen → [[Advisor-Agent-gegen-Drift]]
- Reasoning-Spuren sind kein verlässlicher Drift-Indikator; Prävention schlägt reine Sichtbarkeit → [[Advisor-Agent-gegen-Drift]]
- Widerspruchs- und Entscheidungsregeln in Agent-Hierarchien vorab festlegen statt dem Modell überlassen → [[Kontrollierte-Agent-Parallelisierung]]

## Verbindungen

- [[Advisor-Agent-gegen-Drift]]
- [[Kontrollierte-Agent-Parallelisierung]]
- [[2026-02-07-daniel-san-agent-teams-praxismuster]]
