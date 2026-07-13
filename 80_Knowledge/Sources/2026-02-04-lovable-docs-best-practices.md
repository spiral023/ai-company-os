---
url: https://docs.lovable.dev/tips-tricks/best-practice
autor: "Lovable Docs"
datum: 2026-02-04
erfasst: 2026-07-13
typ: artikel
---

# Lovable Docs zu „Best Practices für Lovable“

## Inhalt

Die **Knowledge-Datei** wird mit jedem Prompt gesendet und ist quasi der PRD-Ersatz des Projekts (Produktvision, User Journeys, Kernfunktionen, Design-System, rollenspezifisches Verhalten); lässt sich automatisch generieren mit „Generate knowledge for my project at T=0 based on the features I've already implemented.“

Plan-Modus als KI-Co-Pilot ohne Code-Änderung: Wechsel empfohlen nach 2-3 gescheiterten Korrekturversuchen oder bei komplexer Logik/Datenbankproblemen. **Viele Nutzer verbringen 60-70% der Zeit im Plan-Modus** und klicken erst auf „Implement the plan“, wenn sie voll zufrieden sind. Kontrollformulierungen: „Investigate but don't write code yet“, „Suggest 3 ways to solve this without changing anything.“

Supabase-Fallstricke: kein sauberes Revert — Zurücksetzen kann das DB-Schema brechen; deshalb Supabase erst verbinden, wenn das Frontend stabil ist (Build-Strategie „Frontend First“: mit Mock-Daten starten, Layouts/Flows/Logik ohne DB bauen, erst danach Supabase verbinden — vermeidet komplexe SQL-Fehler zu Beginn).

„In Bricks bauen“: ein Brick = ein Feature/eine Komponente/ein Flow, nacheinander bauen und testen statt alles gleichzeitig. Fehlerschleifen vermeiden: nicht 10× „Try to Fix“ klicken, sondern Logs/Konsolenfehler in den Plan-Modus geben. Bei verstricktem Zustand: „Remix“ (saubere Kopie des Projekts bei T=0) statt weiterer Korrekturschleifen. Vor dem Start: 15 Minuten außerhalb von Lovable die Idee fixieren (Was tut das Produkt? Für wen? Was ist das MVP?), ggf. daraus mit Claude/GPT ein PRD erstellen lassen.

## Kernaussagen

- Die Lovable-Knowledge-Datei fungiert als projektweiter PRD-Ersatz, der mit jedem Prompt automatisch mitgesendet wird — Produktvision, User Journeys, Design-System und Rollen in einer Datei statt in jedem Prompt neu erklärt → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- 60-70% der Zeit im Plan-Modus zu verbringen, bevor überhaupt implementiert wird, ist die beobachtete Norm bei erfahrenen Nutzern — nicht die Ausnahme → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- „In Bricks bauen“ (ein Feature/eine Komponente nach der anderen, einzeln testen) statt alles gleichzeitig zu implementieren → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Frontend-First-Strategie mit Mock-Daten, Supabase erst nach UI-Stabilität verbinden — vermeidet SQL-Fehler und das Fehlen von sauberem Revert bei Schema-Änderungen → [[Lovable-Prototyp-dann-lokaler-Handoff]]
