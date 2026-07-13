---
name: produktentwicklung
description: Verwende diesen Skill, wenn aus einer Idee ein konkretes digitales Produkt, eine SaaS-Webapp, eine Shopify App oder ein Website-Redesign entstehen soll. Unterstützt Brainstorming, Zielgruppenklärung, Feature-Auswahl, PRD, Roadmap, MVP-Schnitt, Risiken und nächste Schritte.
---

# Produktentwicklung

## Ziel

Verwandle unstrukturierte Ideen in umsetzbare Produktkonzepte.

## Tiefenstufen

Aufwand passend zum Vorhaben wählen, nicht immer alles abfragen:

- **Quick** (5–10 Min): nur Start, Kontext, Ziele.
- **Normal** (15–30 Min): zusätzlich Nutzer, Flows, Daten, Grenzen.
- **Deep** (~60 Min): zusätzlich Integrationen, UI/UX, Technik im Detail, Edge Cases.

Bei trivialen oder bereits vollständig spezifizierten Aufträgen: Tiefenstufen überspringen und direkt umsetzen.

## Abschnitte & Leitfragen

1. **Start** — Projekttitel, Kurzbeschreibung, Lösungsart (Webapp, Windows-App, Automation, Browser-Extension, Agent Skill, Excel-Lösung, API/Service, Hybrid), Ziel der Lösung.
2. **Kontext & Problem** — Worum geht es, wer ist betroffen, wie oft? Welches Problem wird gelöst (mit Zahlen: Zeit, Fehlerquote, Häufigkeit)? Heutiger manueller Ablauf Schritt für Schritt. Was darf auf keinen Fall passieren?
3. **Ziele & Erfolg** — Was soll der Nutzer am Ende tun können? Wichtigstes Ergebnis im MVP? Woran erkennt man Erfolg? Priorität (Must/Should/Could/Won't).
4. **Nutzer & Rollen** — Hauptnutzer, Nutzerkreis (Einzelperson/Team/Extern/Gemischt), Rollen/Berechtigungen, Freigabeprozesse.
5. **Prozess & Flows** — die 1–3 wichtigsten Abläufe Schritt für Schritt: Trigger, Eingaben, Verarbeitung, Ausgabe, Sonderfälle/Benachrichtigungen.
6. **Daten & Schema** — welche Daten rein, welche raus, sensible Daten? Datenhaltung (lokal/Datei/DB/API/Cloud), Schema, Import-/Export-Formate.
7. **Integrationen** — anzubindende Systeme, Authentifizierung, Rate Limits/Restriktionen.
8. **UI/UX** — nur bei Webapp/Browser-Extension/Hybrid relevant: Theme, Navigation, UI-Bausteine.
9. **Technik & Betrieb** — Backend nötig? Hosting, Offline-Fähigkeit, Multi-User, Testtiefe.
10. **Grenzen & Risiken** — was gehört NICHT zum MVP? Annahmen, Hauptrisiken, offene Fragen.
11. **Ausgabe** — Einzeldatei, mehrere Dateien (je Abschnitt) oder Master-Prompt für Coding Agents.

Fragen/Abschnitte überspringen, die von der Lösungsart nicht betroffen sind (z. B. keine UI-Fragen bei reiner Automation/API, keine Integrationsfragen ohne externe Systeme).

## Kalibrierungstechnik: Bad/Good-Beispiele

Bei vagen oder zu knappen Antworten ein Bad/Good-Beispielpaar zur jeweiligen Frage zeigen statt die Frage nur zu wiederholen — kalibriert das erwartete Detailniveau schneller als eine abstrakte Nachfrage. Beispiel: „Tool für Daten" (bad) vs. „Webapp, die CSV-Dateien aus drei Quellen zusammenführt, Dubletten erkennt und ein bereinigtes Excel exportiert" (good).

## Wenn Informationen fehlen

Nutze den Skill `ask-user-question`.

## Ausgabeformat

- Kurzbeschreibung
- Zielgruppe
- Problem
- Nutzenversprechen
- MVP-Features
- Spätere Features (Nicht-MVP)
- Annahmen
- Risiken
- Offene Fragen
- Nächster sinnvoller Schritt
