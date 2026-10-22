# Was kostet KI heute? — RAITEC

Lokaler HyperFrames-Erklärfilm, 9:16, 1080 × 1920, 30 fps, 45,8 Sekunden. Deutsche Sprecherstimme George (ElevenLabs), wortweise synchronisierte Untertitel, sechs editierbare Szenen.

## Ansehen

- MP4: `renders/raitec-ki-kostenentwicklung-9x16.mp4`
- Szenenübersicht: `renders/storyboard/contact-sheet.jpg`
- Abspielseite: `review.html`, mit lokalem Webserver öffnen.
- Studio: `npx hyperframes preview --background`

## Inhalt

1. Was kostet KI heute?
2. Datierter Rückgang der Kosten vergleichbarer Benchmark-Leistung.
3. Klar gekennzeichnetes Rechenbeispiel: Kostenindex 100 → 8.
4. Denkaufwand, Kontext und Versuche als Verbrauchstreiber.
5. Kosten je akzeptiertem Ergebnis als praktische Kennzahl.
6. RAITEC-Abschluss.

Quellen, Grenzen und Ableitung: [SOURCES.md](SOURCES.md). Die Einzelmodell-Preislisten aus dem Repo wurden nicht als aktuelle Tarife ausgegeben.

## Bearbeiten und rendern

`build.mjs` enthält Inhalte, Bildideen und Animationen. Die Sprachaufnahme liegt in `assets/narration.wav`, die tatsächlichen Wortzeitmarken in `assets/narration.words.json`. Sie müssen bei Textänderungen gemeinsam erneuert werden. `assets/audio-provider.json` dokumentiert die verwendete Stimme; Zugangsdaten sind nicht enthalten.

```powershell
npm run build
npm run check
npx hyperframes snapshot --at 4.05,13.54,22.25,30.56,42.13,45 --describe false --output renders/storyboard
npx hyperframes preview --background
npm run render -- --quality delivery --workers 3 --output renders/raitec-ki-kostenentwicklung-9x16.mp4
npm run finish
npm run verify
```

Der Build erzeugt `index.html`, sechs Dateien unter `compositions/frames/`, `SCRIPT.md`, `STORYBOARD.md`, `timing.json` und `audio_meta.json`. Das zentrale RAITEC-`frame.md`, Original-SVGs, lokale Titillium-Web-Schriften und GSAP bleiben im Projekt. Die Registry-Komponente `decline-chart` lieferte das Path-Draw-Prinzip; die Berechnung, lineare Skala, Beschriftung und Darstellung wurden für den Film angepasst.

`finish.mjs` normalisiert die exportierte Tonspur auf −16 LUFS. Der Videostream wird dabei ohne erneute Bildkodierung kopiert. `verify.mjs` misst die tatsächlich gelieferte Datei und schreibt `renders/verification.json`.

Audios, MP4 und große lokale Renderdateien sind gemäß Repo-Regeln nicht versioniert. Keine Veröffentlichung, kein Commit, kein Push.
