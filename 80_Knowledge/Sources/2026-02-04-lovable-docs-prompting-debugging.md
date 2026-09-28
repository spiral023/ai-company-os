---
url: https://docs.lovable.dev/prompting/prompting-debugging
autor: Lovable Docs
datum: 2026-02-04
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/URL/2026-02-04-lovable-docs-prompting-debugging.md
thema: Arbeitsweisen
zeitkritisch: nein
beleg_art: sekundaerquelle
---

# Lovable-Debugging: Plan-Modus, Audit-Prompts und Ursache statt Symptom

Deutsche Aufarbeitung (vibedeck, Sekundärquelle) der Lovable-Doku zum Debugging. Sammlung von Prompt-Vorlagen und Vorgehen bei hartnäckigen Fehlern; Herstellerempfehlung ohne Messung.

## Kernaussagen
- Für Audits (Architektur, Performance) den Plan-Modus nutzen und ausdrücklich „ohne Codeänderung“ berichten lassen → [[Plan-first-mit-getrenntem-Review]]
- Bei kritischen Bereichen (Auth, Payment) Vorsicht und Änderungsgrenzen im Prompt benennen → [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- Bei Fehlerschleifen: bisherige Lösungsversuche abfragen, Ursache erklären lassen, Root Cause statt Symptom fixen, Versionshistorie zum Rollback nutzen

## Einordnung
Die Vorlagen sind plausibel, aber stark auf Lovable zugeschnitten. „Proceed with utmost caution“ ist eine weiche Anweisung; harte Absicherung geben nur Tests oder Rollback.

## Verbindungen
- [[Freiheitsgrad-nach-Aufgaben-Fragilitaet]]
- [[Lovable-Prototyp-dann-lokaler-Handoff]]
- [[2026-02-04-lovable-docs-best-practices]]
