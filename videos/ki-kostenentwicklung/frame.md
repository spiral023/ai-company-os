---
version: 1.0
name: RAITEC — Frame (video / frame layer)
description: >
  HyperFrames-Designsystem für RAITEC-Videos. Grundlage ist das lokale CI-Paket
  (raitec-corporate-identity): Farbtabelle, Titillium Web, Avallon Alt (nur Key-Visual),
  Original-Logo-SVGs. Belegte CI-Werte und lokale Gestaltungsempfehlungen sind im Text
  getrennt gekennzeichnet. Die Einheit ist der Frame (1920×1080).
unit: the frame — 1920×1080 primary; 1080×1920 and 1080×1080 documented
principle: CI-Werte sind fest · Komposition ist frei · Zahlen und Claims kommen nur aus der Quelle

colors:
  # — CI-Palette (HEX-Spalte der gelieferten Farbtabelle) —
  navy: "#05345d"          # Blau 100 — Grund des dunklen Registers, Text im hellen Register
  navy-80: "#334f76"       # Blau 80 — Flächen, Linien, Raster auf Navy
  navy-60: "#607193"       # Blau 60 — zurückgenommene Flächen
  orange: "#f7a824"        # Orange 100 — DER Akzent (sparsam)
  orange-80: "#faba57"     # Orange 80 — zweite Akzentstufe, Verläufe der Facettenlogik
  orange-60: "#ffcc85"     # Orange 60 — nur nach Bestätigung (offene HEX/RGB-Abweichung)
  slate: "#516f82"         # Grau 100 — Sekundärtext im hellen Register, Diagrammflächen
  slate-80: "#718797"      # Grau 80
  slate-60: "#91a1af"      # Grau 60 — Sekundärtext auf Navy
  # — lokale Ausgabeflächen (keine CI-Farben, nur Arbeitswerte) —
  white: "#ffffff"         # Text auf Navy, Grund des hellen Registers
  mist: "#f4f6f7"          # helle neutrale Fläche (aus raitec-history)
  navy-lift: "#0a416a"     # aufgehellte Navyfläche für Panels auf Navy (aus raitec-history)

typography:
  # Titillium Web — Standard-CI (lokal: assets/fonts/TitilliumWeb-*.ttf)
  display:      { fontFamily: "Titillium Web", px: 104, weight: 700, lineHeight: 1.0, tracking: "-0.01em" }
  headline:     { fontFamily: "Titillium Web", px: 76, weight: 600, lineHeight: 1.08, tracking: "-0.005em" }
  numeral:      { fontFamily: "Titillium Web", px: 200, weight: 700, lineHeight: 0.9, tracking: "-0.02em" }
  subhead:      { fontFamily: "Titillium Web", px: 46, weight: 600, lineHeight: 1.15 }
  body:         { fontFamily: "Titillium Web", px: 36, weight: 400, lineHeight: 1.35 }
  label:        { fontFamily: "Titillium Web", px: 30, weight: 600, lineHeight: 1.2 }
  kicker:       { fontFamily: "Titillium Web", px: 26, weight: 600, tracking: "0.14em", upper: true }
  footnote:     { fontFamily: "Titillium Web", px: 22, weight: 400, lineHeight: 1.3 }
  caption:      { fontFamily: "Titillium Web", px: 38, weight: 600, lineHeight: 1.15 }
  # Avallon Alt — NUR Claim/Headline eines Key-Visuals (vorläufige Datei, siehe Fonts)
  key-visual:   { fontFamily: "Avallon Alt", px: 120, weight: 400, lineHeight: 1.0 }

spacing:
  edge: "100px"            # Action-safe-Rand
  text-edge: "140px"       # Mindestabstand für Haupttexte
  content-bottom: "870px"  # Bild- und Titelinhalte enden darüber
  caption-band: "900px–1010px"
  gap: "40px"
  radius: "12px"           # lokale Empfehlung für Panels/Pills

components:
  facet-lattice:
    pattern: "isometrisches Dreiecksraster (30°-Kanten wie der Würfel), {colors.navy-80}, opacity 0.08–0.14"
    placement: "Hintergrund auf Navy, zur Mitte maskiert"
    description: "Leitet die Facetten der Bildmarke in eine ruhige Fläche ab. Lokale Empfehlung."
  light-line:
    stroke: "{colors.orange}, 4–6px, runde Enden, optional weicher Glow"
    description: "Die orange Verbindungslinie: verbindet Knoten, Jahre, Orte. Signatur-Bewegung (Path-Draw)."
  node:
    shape: "abgerundetes Rechteck (radius 12px) oder Facetten-Raute, Fläche {colors.navy-lift}, Kontur {colors.navy-80}"
    typography: "{typography.label} + {typography.footnote}"
    description: "Station/Einheit in Diagrammen; aktive Knoten mit orangem Rand."
  kicker-rule:
    typography: "{typography.kicker} in {colors.orange} (Navy) bzw. {colors.slate} (hell)"
    rule: "3px {colors.orange}, 64px breit, links vor oder über dem Kicker"
    description: "Kapitelmarke über jeder Headline."
  data-bar:
    fill: "{colors.orange} (Fokuswert) · {colors.slate-60} auf Navy bzw. {colors.slate} hell (Vergleichswerte)"
    baseline: "2px {colors.slate-60}"
    description: "Balken mit flachen Enden; Werte in {typography.subhead}."
  caption-pill:
    surface: "{colors.navy}, radius 12px, keine Schatten"
    text: "{colors.white}, {typography.caption}; aktives Wort {colors.orange}"
    description: "Untertitel im Band 900–1010px."
  logo:
    asset: "assets/brand/raitec-logo-*.svg (Original, unverändert)"
    description: "Weiße Ausführung auf Navy, farbige Ausführung auf hell. Nie nachbauen, umfärben, verzerren."
  end-card:
    composes: "Logo-Lockup zentriert, darunter {typography.body} Website-Zeile www.raitec.at in {colors.slate-60}"
    description: "Schlusstafel. Nur belegte Angaben (Website), keine erfundenen Claims."
---

# RAITEC — Frame (video / frame layer)

## Overview

RAITEC-Videos wirken **ruhig, verlässlich und technisch präzise**: Banken-IT, Rechenzentrum, Netzwerk. Der Standard ist das **dunkle Register** auf Navy (`{colors.navy}`) mit weißer Schrift und **einem** orangen Akzent pro Frame. Für Aussagen, Zitate und Übersichten gibt es ein **helles Register** (`{colors.white}` / `{colors.mist}` mit Navy-Schrift).

Die Bildsprache leitet sich aus der Bildmarke ab: **Facetten, 30°-Kanten, die drei Würfelflächen**. Die Signatur in Bewegung ist die **orange Lichtlinie**, die Dinge verbindet (Knoten, Jahre, Standorte). Das ist eine lokale Gestaltungsempfehlung auf Basis der Bildmarke, keine belegte offizielle Bildsprache.

**Belegt (CI-Paket):** Farbtabelle, Schriftrollen, Original-Logos.
**Lokale Empfehlung:** Register, Facettenraster, Lichtlinie, Radien, Größen, Treatments.

## The Frame

### Frame Craft Bar

- **Squint:** ein Element dominiert (Headline, Zahl oder Diagramm) mit klarer Hierarchie über Größe *und* Gewicht.
- **Ein Akzent:** Orange markiert genau eine Sache pro Frame (das Schlüsselwort, die aktive Linie, den Fokuswert). Orange ist nie Flächenfarbe für große Hintergründe.
- **Ruhe:** großzügige Ränder, 40–55 % ruhige Fläche bei Aussage-Frames; Diagramm- und Daten-Frames dürfen dichter sein.
- **Referenz:** seriöser Corporate-Film eines IT-Dienstleisters für Banken. Fehlbild: bunte Startup-Ästhetik, Neon, leuchtende Gehirne, Roboter.

### Maße

- **Primär:** 1920×1080. Werte in px beziehen sich auf diese Größe.
- **Ränder:** 100px action-safe; Haupttexte ≥ 140px vom Rand.
- **Untertitel-Band:** y 900–1010px. Bild- und Titelinhalte bleiben **oberhalb von y 870px**.
- **Mindestgröße** für tragenden Text: 28px (`kicker` und `footnote` sind Ausnahmen für Chrome).

## Colors

- **Navy** ist der Grund (dunkles Register) bzw. die Textfarbe (helles Register).
- **Weiß** ist die Textfarbe auf Navy. **Slate-60** ist Sekundärtext auf Navy; **Slate** Sekundärtext auf hell.
- **Orange** ist der einzige Akzent: Schlüsselwort, Lichtlinie, Fokuswert, Kicker-Linie. **Orange-80** nur als zweite Stufe neben Orange 100 (z. B. zweiter Balken, Facettenpaare).
- **Navy-80 / Navy-lift** für Panels, Raster und Konturen auf Navy.
- **Orange-60** erst verwenden, wenn die offene HEX/RGB-Abweichung bestätigt ist.
- 80-%- und 60-%-Stufen sind **feste Farbwerte** — nie durch Opacity oder Mischungen ersetzen.
- `white`, `mist`, `navy-lift` sind lokale Arbeitswerte, **keine** zusätzlichen CI-Farben.
- Die Logo-SVGs behalten ihre eigenen Werte (`#f7a823`, `#faba58`), auch wenn sie minimal von der Tabelle abweichen.

## Typography

- **Titillium Web** für alles: Display/Headline 600–700, Fließtext 400, Labels/Kicker 600. Kicker in Versalien mit 0.14em Laufweite.
- **Avallon Alt** ausschließlich für Claim/Headline eines Key-Visuals (Anfangs- oder Schlusstitel), nie für Fließtext. Die Datei ist **vorläufig** (Quelle: „Personal use only“); bis die lizenzierte RAITEC-Datei vorliegt, nur für interne Entwürfe. Im Zweifel Titillium Web Bold verwenden.
- Keine anderen Schriften. Keine Systemschrift-Fallbacks im Render: Schriften immer lokal laden.
- Headlines in Satzschreibung (nicht alles in Versalien), maximal ~6 Wörter pro Zeile, maximal 2 Zeilen.

### Fonts & Assets (Pfade im Projekt)

Das Setup-Skript (`apply.mjs`) legt alles lokal ab:

```css
@font-face { font-family: "Titillium Web"; src: url("assets/fonts/TitilliumWeb-Regular.ttf") format("truetype"); font-weight: 400; }
@font-face { font-family: "Titillium Web"; src: url("assets/fonts/TitilliumWeb-SemiBold.ttf") format("truetype"); font-weight: 600; }
@font-face { font-family: "Titillium Web"; src: url("assets/fonts/TitilliumWeb-Bold.ttf") format("truetype"); font-weight: 700; }
@font-face { font-family: "Titillium Web"; src: url("assets/fonts/TitilliumWeb-Light.ttf") format("truetype"); font-weight: 300; }
/* nur wenn mit --avallon eingerichtet: */
@font-face { font-family: "Avallon Alt"; src: url("assets/fonts/AvallonAlt-provisional.ttf") format("truetype"); font-weight: 400; }
```

- Logos: `assets/brand/raitec-logo-with-subline-white.svg`, `…-color.svg`, `raitec-logo-without-subline-*.svg`, `raitec-mark-color.svg`
- GSAP lokal: `assets/vendor/gsap.min.js` (statt CDN, damit offline gerendert werden kann)
- Pfade sind relativ zum Projektordner, auch in `compositions/frames/*.html`.

## Depth & Surface

- **Flach.** Keine Schlagschatten, keine Glas-/Blur-Effekte, keine Farbverläufe als Flächen.
- Erlaubt: eine sehr dezente **radiale Vignette** auf Navy und ein weicher **Glow** an der orangen Lichtlinie.
- Tiefe entsteht über Flächen-Stufen (Navy → Navy-lift → Navy-80) und Überlagerung.

## Shapes

- Facetten-Dreiecke und 30°-Diagonalen (isometrisch wie der Würfel) als Formvokabular.
- Panels, Knoten und Pills mit **12px Radius** (lokale Empfehlung, passt zu den leicht gerundeten Facetten der Bildmarke).
- Linien mit runden Enden.

## Components

- **facet-lattice:** ruhiges isometrisches Dreiecksraster im Hintergrund, zur Mitte maskiert.
- **light-line:** orange Verbindungslinie, zeichnet sich (Path-Draw) und verbindet Knoten.
- **node:** Station im Diagramm (Navy-lift, Navy-80-Kontur, aktiv mit orangem Rand).
- **kicker-rule:** Kicker mit kurzer oranger Linie über jeder Headline.
- **data-bar:** flache Balken, Fokuswert Orange, Vergleichswerte Slate.
- **caption-pill:** Untertitel auf Navy-Pill, aktives Wort Orange.
- **logo / end-card:** Original-SVG, Schlusstafel mit www.raitec.at.

## Frame Treatments

> Rezept: Grund · Komposition · Fokus · Chrome · Akzent · Ruhe · Fest/Frei · Dichte.

### 1 · Key Visual / Titel (dunkel)
**Grund** Navy + facet-lattice + Vignette. **Komposition** Titel links (ab 140px), rechts Raum für Motiv oder Bildmarke. **Fokus** `display` (oder `key-visual` Avallon für den Claim), darunter `subhead` in Slate-60. **Chrome** Kicker mit Kicker-Linie. **Akzent** ein Wort in Orange oder die Lichtlinie. **Ruhe** ~50 %. **Fest** Navy-Grund, Titillium. **Frei** Motiv, Linienführung. **Dichte** sparsam.

### 2 · Kapitel / Jahreszahl (dunkel)
**Grund** Navy. **Fokus** `numeral` (z. B. „2015“) in Weiß oder Orange, daneben/darunter `headline` mit 2–5 Wörtern. **Chrome** Kicker. **Akzent** Lichtlinie läuft zur Zahl. **Ruhe** ~55 %. **Dichte** sparsam.

### 3 · Verbindung / Diagramm (dunkel)
**Grund** Navy. **Fokus** 3–5 Knoten, verbunden durch die Lichtlinie; der aktive Knoten orange gerandet. **Chrome** Kicker + `headline` oben links. **Akzent** die Linie selbst. **Dichte** mittel — jeder Knoten braucht `label` ≥ 30px.

### 4 · Daten (dunkel oder hell)
**Grund** Navy oder Weiß. **Fokus** 2–6 data-bars oder eine große Kennzahl (`numeral`) mit Einheit. **Chrome** Kicker + Quelle als `footnote`. **Akzent** nur der Fokuswert in Orange. **Fest** Zahlen nur aus der Quelle. **Dichte** mittel.

### 5 · Aussage / Zitat (hell)
**Grund** `white` oder `mist`. **Fokus** `headline` in Navy, 2–3 Zeilen, ein Schlüsselwort in Orange. **Chrome** Kicker in Slate, Quellenzeile `footnote`. **Ruhe** ~55 %. **Dichte** sparsam.

### 6 · Abschluss / Endkarte (dunkel)
**Grund** Navy + facet-lattice. **Fokus** Logo-Lockup (weiß, Original) zentriert, ~900–1200px breit. **Chrome** `body` „www.raitec.at“ in Slate-60 darunter. **Ruhe** ~60 %, mindestens 2 s ruhiger Stand. **Fest** Original-Logo, keine weiteren Claims ohne Freigabe.

## Motion

- **Eintritte:** opacity + 20–40px Versatz, 0.5–0.9s, `power3.out`. Keine Bounce-/Elastic-Eases.
- **Lichtlinie:** Path-Draw 1–2s, `power2.inOut`; Knoten erscheinen, wenn die Linie sie erreicht.
- **Facetten:** Dreiecke dürfen sich zu Flächen zusammensetzen (Assembly), immer auf 30°-Achsen.
- **Logo:** nur Einblenden, gleichmäßiges Skalieren, Verschieben. Facetten-Animationen nur, wenn sie exakt im Original enden (siehe `videos/raitec-logo-sting`, `raitec-logo-3d`, `raitec-logo-fold`).
- **Holds:** Stillstand statt Dauerbewegung; keine langsamen Kamerafahrten in der zweiten Hälfte einer Szene.
- **Übergänge:** Schnitt, Crossfade, Push-Slide. Keine Effekt-Wipes.

## Composition Rules

### Do
- Navy-Grund als Standard; helles Register gezielt für Aussagen und Übersichten.
- Genau ein oranger Akzent pro Frame.
- Titillium Web lokal laden; Avallon Alt nur für den Key-Visual-Claim.
- Original-Logo-SVGs verwenden (weiß auf Navy, farbig auf hell).
- Inhalte oberhalb von y 870px; Untertitel im Band 900–1010px.
- Quellen für Zahlen als `footnote` angeben.

### Don't
- Keine zusätzlichen Farben (kein Grün/Rot/Lila, keine Neon-/KI-Verläufe).
- Kein Orange als großflächiger Hintergrund.
- Logo nicht nachbauen, umfärben, drehen, verzerren oder mit Effekten versehen.
- Keine erfundenen Claims, Kennzahlen oder Kundennamen.
- Keine generischen Stock-Motive (leuchtende Gehirne, Roboter, Binärcode-Regen).
- Keine Schlagschatten, keine Glassmorphism-Effekte.

## Aspect-Ratio Behavior

| Treatment | 16:9 | 9:16 | 1:1 |
| --- | --- | --- | --- |
| Key Visual | Titel links, Motiv rechts | Titel oben, Motiv unten | Titel oben, Motiv unten |
| Kapitel | Zahl links, Headline rechts | Zahl oben, Headline darunter | gestapelt, zentriert |
| Diagramm | Knoten horizontal | Knoten vertikal | 2×2-Raster |
| Daten | Balken horizontal | Balken vertikal, weniger Werte | Kennzahl zentriert |
| Aussage | links ausgerichtet | zentriert, größer | zentriert |
| Endkarte | Lockup zentriert | Bildmarke oben, Schriftzug darunter | Lockup zentriert |

9:16-Untertitel-Band: y ≈ 1500–1700px; Inhalte bleiben darüber.

## Approved Entities

- **Unternehmen:** RAITEC (Schreibweise in Versalien). Website: www.raitec.at.
- **Belegte Leistungsbereiche** (Selbstauskunft, Stand 13.10.2026, `wallpapers/research-raitec.md`): Rechenzentrumsbetrieb, Netzwerk, Server/Storage/Mainframe, Managed Cloud, Electronic Banking/Zahlungsverkehr, Druck & Kuvertierung, dezentrale IT bis zum Arbeitsplatz. Standorte: Linz (Sitz), Graz/Raaba, Innsbruck, Klagenfurt, Salzburg.
- **Aussprache im Sprechertext:** GRZ → „Ge Er Tsett“, RAITEC → „Raiteck“, RACON → „Raakon“ (siehe `docs/sprachausgabe-stimmen.md`).

## Numerals & Claims (hard rule)

Keine erfundenen Zahlen, Daten, Claims oder Superlative. Werte kommen ausschließlich aus der gelieferten Quelle; sonst Platzhalter (`— Wert —`). Werbesuperlative von Webseiten werden nicht übernommen.

## Pre-Render Self-Audit

- **Farben:** nur Palette + lokale Arbeitswerte; genau ein oranger Akzent.
- **Schrift:** Titillium Web lokal geladen; Avallon nur im Key-Visual; tragender Text ≥ 28px.
- **Logo:** Original-SVG, unverändert, richtige Ausführung für den Grund.
- **Layout:** Inhalte oberhalb y 870px; Ränder ≥ 100px.
- **Tiefe:** keine Schatten, keine Verläufe als Flächen.
- **Inhalt:** jede Zahl und jeder Claim aus der Quelle belegt.
- **Bewegung:** power3, keine Bounces, Endstände ruhig.

## Known Gaps

- Kein offizielles Brand-Manual: Schutzraum, Mindestgröße des Logos, verbindliche Claims und Bildsprache sind nicht festgelegt. Die Regeln oben sind lokale Empfehlungen.
- Avallon Alt ist eine vorläufige Datei ohne nachgewiesene kommerzielle Lizenz.
- Orange 60: HEX/RGB-Abweichung in der Farbtabelle ungeklärt.
