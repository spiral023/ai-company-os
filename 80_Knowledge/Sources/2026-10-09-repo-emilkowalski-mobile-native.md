---
url: https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/mobile-native/SKILL.md
autor: Emil Kowalski
datum: 2026-10-09
erfasst: 2026-10-09
typ: repo
thema: Arbeitsweisen
zeitkritisch: nein
---

# Mobile-Webapps nach Eingabefähigkeit und tatsächlichem Browserverhalten prüfen

Read-only-Prüfung von `external_repos/emilkowalski/skills/skills/mobile-native/SKILL.md` am 09.10.2026, Checkout `e8a175de22ae1e49370fc144c1f3bb9aeedf988d`. Das Datum bezeichnet den Abgleich, nicht die ursprüngliche Veröffentlichung. Der Skill beschreibt gezielte CSS- und HTML-Korrekturen für mobile Webapps; weder der Skill noch fremde Scripts wurden ausgeführt.

## Eingabe, Höhe und sichere Ränder getrennt behandeln

Hover-Effekte werden im Skill über `(hover: hover)` und `(pointer: fine)` an die Eingabefähigkeit gebunden. Touch-Nutzer brauchen eigenes Druckfeedback; Textinhalt soll auswählbar bleiben. Zoom darf nicht über `user-scalable=no` oder `maximum-scale=1` abgeschaltet werden. Für kleine Eingabeschriften nennt der Autor `16px` als Ausgangswert, der im jeweiligen Browser zu prüfen ist.

Der Skill unterscheidet eine dynamische App-Höhe mit `dvh` von einer stabilen kleinen Viewporthöhe mit `svh`. Randfüllende Layouts kombinieren `viewport-fit=cover` mit `env(safe-area-inset-*)` für betroffene feste Bedienelemente. Eigene Innenabstände bleiben zusätzlich nötig. `touch-action: manipulation` und Einschränkungen des Scrollens sollen nach konkretem Symptom ausgewählt werden; eine globale Übernahme des gesamten Baseline-Beispiels ist keine geprüfte Verbesserung.

## Abgleich mit Plattformdokumentation

Die folgenden Dokumentationsstellen wurden am 09.10.2026 zur technischen Gegenprüfung gelesen; sie sind ergänzende Referenzen und kein behaupteter vollständiger Import dieser Seiten:

- [MDN zu hover](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/hover): Die Abfrage beschreibt den primären Eingabemechanismus. Mischgeräte mit Touch und Maus brauchen zusätzliche praktische Prüfung.
- [MDN zu CSS-Längeneinheiten](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length): `vh` entspricht der großen Viewportvariante; `dvh` kann seine Größe mit ein- und ausfahrenden Browserleisten ändern. `svh` orientiert sich an der kleinen Variante.
- [MDN zu meta viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport): Bildschirmtastatur, visueller Viewport und Layout-Viewport sind zu unterscheiden. `interactive-widget` beeinflusst das Verhalten, dessen Unterstützung im Zielbrowser geprüft werden muss; `dvh` allein ist keine universelle Tastaturlösung.
- [MDN zu touch-action](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/touch-action): `manipulation` erlaubt Panning und Pinch-Zoom, deaktiviert aber Double-Tap-Zoom. `none` unterbindet browserseitige Gesten auf der betroffenen Fläche.
- [WebKit zu sicheren Rändern](https://webkit.org/blog/7929/designing-websites-for-iphone-x/): Randfüllende Inhalte brauchen mit `viewport-fit=cover` gezielte sichere Innenabstände. Die Insets ersetzen keine normalen Layoutabstände.

## Einordnung

Verifiziert ist der dokumentierte Ablauf im vorhandenen Repo, keine ausgeführte Abnahme und keine Umwandlung zur Native-App. Browser-Emulation eignet sich für Layoutbreiten; reale Tastatur-, Touch- und Browserleisteninteraktionen gehören auf Zielhardware geprüft. Einzelne pauschale Formulierungen des Skills, etwa dass keines der Symptome in Emulation reproduzierbar sei, werden hier nicht als allgemeine Browsergarantie übernommen. Eine produktive Installation oder Lizenzfreigabe des externen Skills ist mit dieser Inhaltsprüfung nicht verbunden.

## Kernaussagen

- Eingabe- und Viewportprobleme anhand konkreter Symptome beheben und anschließend auf realer Hardware prüfen → [[Mobile-Webapp-nach-Eingabefaehigkeit-pruefen]]
- Layoutprüfung mit Extremdaten und Prüfung des mobilen Browserverhaltens sind ergänzende Aufgaben → [[UI-Grenzfaelle-mit-realistischen-Daten-pruefen]]

## Verbindungen

- [[2026-10-04-emilkowalski-2106752670405099523]]
- [[Mobile-Webapp-nach-Eingabefaehigkeit-pruefen]]
- [[UI-Grenzfaelle-mit-realistischen-Daten-pruefen]]
