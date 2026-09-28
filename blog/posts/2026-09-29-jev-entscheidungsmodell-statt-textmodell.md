---
titel: "Jev: ein Modell für typisierte Entscheidungen statt Text"
datum: 2026-09-29
kategorie: kurz
zusammenfassung: "TypeSafe AI liefert mit Jev ein Modell, das für kleine Urteile typisierte Antworten mit Wahrscheinlichkeiten ausgibt. Die Zahlen sind Herstellerangaben ohne unabhängige Messung."
status: entwurf
quellen:
  - 2026-09-18-akshay_pachaar-2101037514945597645
---

Jev von TypeSafe AI erzeugt keinen Text. Für vorab definierte Fragen liefert es typisierte Antworten mit Wahrscheinlichkeiten: Choice (eine Option aus einer Liste), Score (Wert auf einer Skala) und Noul (Ja/Nein als Wahrscheinlichkeit). Der Code behält die Verzweigung, das Modell liefert das unscharfe Urteil. Genannte Einsatzplätze sind Model Routing, Risiko-Gating vor Tool-Calls, Verifikation, Reranking und Triage.

Alles Folgende sind Herstellerangaben, wiedergegeben in einem Artikel von Akshay Pachaar, einer wohlwollenden Drittdarstellung: Latenz 70 bis 500 ms, `$0.042` pro Million Input-Token, Output kostenlos, angeblich rund 200-mal schneller und 400-mal günstiger als vergleichbare LLM-Workflows. Laut Artikel stammen die Multiplikatoren aus TypeSafes eigenen Evals und vom günstigen Ende. Unabhängige Messungen und die Methodik fehlen, ebenso ein Beleg für die versprochene Kalibrierung. Das Modell hat Closed Weights und läuft im Early Access, Input nur Text/JSON.

Die Grenzen nennt der Artikel selbst: „Kann nicht halluzinieren“ gilt nur für das Schema, eine sicher falsche gültige Option ist möglich. Bei Arithmetik, Zählen, Datumsvergleich und mehrstufigem Schließen ist Jev unzuverlässig.

Das Prinzip (feste Antworttypen, explizite Unsicherheit, Schwellen im Code) ist unabhängig vom Produkt plausibel. Wenn du es ausprobierst: Shadow Mode, Kalibrierungskurve auf eigenen Daten, dann die sicherste Verzweigung zuerst automatisieren. Permissions und Sandbox ersetzt es nicht.
