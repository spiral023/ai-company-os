---
url: https://www.tiktok.com/@promptgefluester/video/7664997418081062177
autor: "@promptgefluester"
datum: 2026-07-21
erfasst: 2026-08-29
typ: video
rohquelle: 00_Inbox/Quellen/TikTok/2026-07-21-promptgefluester-prompt-engineering-ist-tot-und-keiner-hats-gemerkt-was-meine-ich-damit.md
thema: Arbeitsweisen
zeitkritisch: nein
---

# Prompt Engineering wird durch Frage-Skills und Hook-Skills ersetzt

Ein TikTok-Creator argumentiert, ein langer Initial-Prompt sei die schwächste Art, KI-Schwächen auszugleichen, weil das Modell die Regeln vom Anfang im wachsenden Context nicht mehr zuverlässig einhält. Stattdessen setzt er auf zwei Skill-Arten: Skills, die per Rückfragen sauberen Basis-Kontext erzeugen, und hook-basierte Skills, die im laufenden Prozess Regeln nachladen. Die Quelle ist eine Einzelmeinung aus einem 2:30-Video mit automatischem Transkript, ohne Messung oder Beleg.

## Zwei Schichten statt eines großen Prompts

- **Kontext aufbauen per Rückfrage:** Skills wie der Brainstorming-Skill aus Superpowers (und ein weiterer, im Transkript als „Grammy“ geschriebener Skill, vermutlich ein Grilling-Skill; die Zuordnung ist nicht gesichert) führen Feedback Loops. Die KI fragt so lange nach, bis das Problem von allen Seiten beleuchtet ist. Du beschreibst nur das Ergebnis, die KI fragt nach dem, was sie wissen muss.
- **Regeln im Prozess nachladen:** Hook-basierte Skills reichern den Kontext beim Code schreiben, Prüfen, Deployen, Datenbanken anlegen oder Daten lesen immer wieder mit den wichtigsten Regeln an.

## Begründung

Frühes Prompt Engineering kompensierte Modellschwächen mit möglichst viel Kontext vorab. Der Creator hält das für die schwächste Lösung, da der Context mit zunehmender Länge die anfänglichen Regeln nicht mehr einhält. Ein während des Laufs geladener Skill sei daher stärker als ein Initial-Prompt.

## Sammelpraxis

Er hält einen zentralen Skill, in den er aus neu gefundenen Skills (YouTube, TikTok) einzelne Features extrahiert, um die Code-Qualität zu verbessern.

## Einordnung

Die Drift-These (Regeln vom Anfang verlieren an Wirkung) deckt sich mit dem Bestand, ist hier aber nur behauptet, nicht gemessen. „Prompt Engineering ist tot“ ist überzogen: Die Skills sind selbst geschriebene Prompts, die Arbeit verschiebt sich auf Skill-Design, Trigger und Hook-Konfiguration. Kosten bleiben ungenannt: Jeder Hook-Reload belegt Context, und eine Sammlung fremder Skills kann Konflikte und Bloat erzeugen. Der Ansatz der Rückfrage-Schleife ist als Spec-Grilling bekannt.

## Kernaussagen

- Rückfrage-Skills erzeugen den sauberen Basis-Kontext, statt ihn per Prompt vorzuladen → [[Spec-Grilling]]
- Hook-basierte Skills laden Regeln während des Prozesses nach, weil Initial-Regeln im langen Context verblassen → [[Hook-erzwungene-Skill-Aktivierung]]
- Ein zentraler Skill als Sammelstelle für extrahierte Features fremder Skills → [[Skill-Call-Hierarchie]]

## Verbindungen

- [[Spec-Grilling]]
- [[Hook-erzwungene-Skill-Aktivierung]]
- [[Kontext-Hygiene-Entscheidungsbaum]]
- [[2026-07-13-mattpocock-handoff-to-teach]]
