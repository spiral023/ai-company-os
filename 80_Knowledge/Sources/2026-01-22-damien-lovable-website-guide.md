---
url: https://x.com/damienghader/status/2014341010600435925
autor: "Damien Ghader"
datum: 2026-01-22
erfasst: 2026-08-04
typ: tweet
rohquelle: 00_Inbox/Quellen/X/2026-01-22-damien-lovable-website-guide.md
beleg_art: sekundaerquelle
---

# Lovable-Websites: Layout-Vorlagen, Spacing-Regeln und ein Conversion-Baukasten

Diese Notiz fasst eine vibedeck-Aufarbeitung eines X-Threads von @damienghader zusammen — der Inhalt liegt also aus zweiter Hand vor, nicht aus einer direkten Prüfung der Primärquelle. Der Thread bündelt ein Layout- und Conversion-Framework für mit Lovable gebaute Websites: Hero-Varianten, eine empfohlene Sektionsreihenfolge, Spacing-/Typografie-Regeln, feste Breakpoints und ein knapper Iterationszyklus. Der eigentliche Wert für die Arbeitsweise mit KI-Website-Buildern liegt weniger in den Design-Regeln selbst — das ist etabliertes Webdesign- und CRO-Wissen — als in der Art, wie sie als Prompt formuliert werden: konkret und strukturell statt als vage Adjektive.

## Hero-Layout und Sektionsreihenfolge

Der Thread schlägt drei bewährte Hero-Layouts vor: (A) große Headline mit Produkt-Screenshot rechts, (B) zentrierte Headline mit drei Bullet-Points und Screenshot darunter, (C) Split-Layout mit Value Proposition links und Social Proof rechts. Anspruch: Die Hero-Section soll innerhalb von fünf Sekunden drei Fragen beantworten — Was ist das? Für wen? Warum wichtig? Für Layout B liefert die Quelle direkt einen ausformulierten Lovable-Prompt: „Create a hero section using layout option B: Centered headline, 3 concise value bullets, and a product screenshot below. Add a primary CTA button. Keep spacing generous and the layout clean and premium.“

Für die Seite insgesamt schlägt der Thread eine feste Sektionsreihenfolge vor: Hero (Value Proposition + CTA) → Social Proof (Logos, Partner) → Problem/Lösung → Feature-zu-Outcome-Mapping → Visual Demo → Secondary Proof (Testimonials) → finaler CTA.

## Spacing, Typografie und feste Breakpoints

Als größten Fehler bei KI-generierten Seiten nennt die Quelle zu wenig Weißraum. Empfohlen wird generöser vertikaler Abstand zwischen Sektionen und ein Wechsel-Rhythmus (z. B. Light → Dark → Light, Bild links → Bild rechts), damit lange Seiten leichter wirken. Bei der Typografie gilt eine harte Obergrenze: eine Schriftart, drei Größen, zwei Gewichte. Auch dafür liegt ein direkt einsetzbarer Prompt vor: „Use white space, subtle borders, and light/dark section contrast. Avoid heavy gradients and visual noise. Use a single font family and limit typography to three sizes and two weights.“

Für Mobile nennt die Quelle vier konkrete Breakpoints: Desktop ab 1440 px, Tablet ab 1024 px, Mobile Landscape bis 768 px, Mobile bis 375 px. Begründung: Die meisten KI-generierten Seiten scheitern auf dem Smartphone, weil solche Breakpoints im Prompt schlicht nicht definiert werden. Mobile-Regeln dazu: Sektionen kürzen, weniger Text, mehr Spacing, CTAs früher im Scroll-Flow zeigen. Auch hier der Prompt im Wortlaut: „Make the layout fully responsive. Stack elements below 768px. Hide secondary elements on mobile. Use full-width CTA buttons below 480px. Ensure large tap targets.“

## Conversion-Regeln und Iterationszyklus

Vor dem Design soll die Konversionspsychologie geklärt sein: Warum melden sich Nutzer an, was hält sie ab? Konkrete Regeln: Testimonials mit echten Zitaten wirken stärker als Werbetext; jede Seite soll nur eine Aktion pushen; spezifische CTA-Formulierungen („Erstelle Deinen ersten Bericht“) sollen besser konvertieren als generische („Get Started“) — Letzteres bleibt unbelegt, die Quelle nennt keine Zahl dazu, nur die Behauptung.

Als Testreihenfolge für die Iteration nennt der Thread: Headlines → CTA-Wording → Button-Platzierung → Sektionsreihenfolge, mit einem knappen Vierschritt-Zyklus in Lovable: Duplizieren → Anpassen → Shippen → Verfeinern.

## Einordnung

Der Großteil dieses Threads ist generisches, seit Jahren etabliertes Webdesign- und CRO-Wissen (Hero-Patterns, Sektionsreihenfolge, Social Proof, spezifische CTAs), das hier für Lovable neu verpackt wird — keine eigenständige KI-Arbeitsweise. Als Sekundärquelle ist außerdem keine der genannten Zahlen (Fünf-Sekunden-Regel, „1 Schriftart/3 Größen/2 Gewichte“, Breakpoint-Werte) hier selbst in der Primärquelle geprüft worden; sie werden als Behauptung der Quelle wiedergegeben, nicht als gemessenes Ergebnis.

Der tatsächlich übertragbare Kern für die Arbeit mit KI-Website-Buildern sind die vier mitgelieferten Prompt-Beispiele: Sie übersetzen Design-Entscheidungen in konkrete, strukturelle Vorgaben (benannte Layout-Option, exakte Pixel-Breakpoints, feste Typografie-Zahlen) statt vager Adjektive wie „modern“ oder „clean“. Das deckt sich mit einem bereits im Bestand belegten Prinzip aus [[Lovable-Prototyp-dann-lokaler-Handoff]] („klare Layout-Logik statt vager Adjektive“) und der component-first-Quelle desselben Autors ([[2026-01-17-damien-ghader-prompting-lovable-design]], „Tailwind-Terminologie statt vager Adjektive“) — dieser Thread liefert dazu vier weitere konkrete Prompt-Formulierungen, aber keine neue Mechanik. Die feste Sektionsreihenfolge und der Iterationszyklus („Duplizieren → Anpassen → Shippen → Verfeinern“) passen ebenfalls zum Handoff-Pattern als leichte, risikofreie Variantentests vor dem Wechsel in den lokalen Agenten-Workflow, sind aber selbst kein neuer Mechanismus, sondern eine Anwendung des dort bereits beschriebenen „früh sichtbar machen, günstig iterieren“-Gedankens.

## Kernaussagen

- Design-Entscheidungen als konkrete strukturelle Vorgaben statt vager Adjektive prompten — benannte Layout-Option, exakte Typografie-Zahlen („1 Schriftart, 3 Größen, 2 Gewichte“), exakte Pixel-Breakpoints (1440/1024/768/375 px) → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Vierschritt-Iterationszyklus „Duplizieren → Anpassen → Shippen → Verfeinern“ als risikoarmer Variantentest in Lovable, bevor Backend/Deployment relevant werden → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Feste Sektionsreihenfolge (Hero → Social Proof → Problem/Lösung → Feature-Outcome → Demo → Testimonials → CTA) ist etabliertes CRO-Wissen, keine KI-spezifische Arbeitsweise → kein Pattern-Verweis, siehe Einordnung

## Verbindungen

- [[Lovable-Prototyp-dann-lokaler-Handoff]]
- [[2026-01-17-damien-ghader-prompting-lovable-design]]
- [[2026-04-17-wiki-compiler-lovable-design-debugging-sicherheit]]
