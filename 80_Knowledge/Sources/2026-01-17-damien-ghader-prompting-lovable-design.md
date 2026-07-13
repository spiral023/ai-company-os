---
url: https://x.com/damienghader/status/2012547182130336033
autor: "Damien Ghader"
datum: 2026-01-17
erfasst: 2026-07-13
typ: tweet
---

# Damien Ghader zu „The Complete Guide: Prompting Lovable for Design“

## Inhalt

Kernthese: Echte Design-Systeme sind component-first, nicht page-first — genau so funktioniert auch Lovable. Ein Design-System ist kein UI-Kit/keine Figma-Datei, sondern ein Satz von Regeln, die Design-Entscheidungen in wiederverwendbare Logik verwandeln. Drei Ebenen: **Foundations** (Color Tokens, Spacing Scale, Border Radius, Schriftgrößen — unverhandelbare Grundlagen, sollten überall auftauchen, nicht nur einmal), **Komponenten** (Ausdruck der Regeln: Buttons, Cards, Inputs mit Padding-Logik, Hover/Active/Disabled-States), **Komposition** (wie Komponenten zusammenkommen — Dashboard-Layouts, Formular-Gruppierungen; hier scheitern die meisten Apps, weil Komposition erst funktioniert, wenn Komponenten stabil sind).

Ohne Design-System erfindet die KI Styles, Komponenten driften auseinander; mit System verstärkt die KI Muster und verbessert Konsistenz über Zeit. Praxisregel: Komponenten prompten statt ganzer Seiten („Create a primary button component with hover, active, and disabled states“ statt „Design a modern dashboard page“), in Tailwind-Terminologie statt vager Adjektive wie „sauber/modern/minimal“ prompten, existierende Komponenten namentlich referenzieren („using the same layout as TotalAmountCard.tsx“ — bewahrt Spacing, Proportionen, visuellen Rhythmus), Styling-Logik kopieren statt neu designen (sagen woher kopiert werden soll, nicht was designt werden soll — reduziert Fehler drastisch), globale Komponenten (Navbar, Sidebar, Buttons) zuerst reparieren, bevor einzelne Seiten gebaut werden, Vorher/Nachher-Screenshots mit benannten Deltas nutzen.

## Kernaussagen

- Design-Systeme sind component-first (Foundations → Komponenten → Komposition), nicht page-first — Komposition scheitert typischerweise, weil sie vor stabilen Komponenten versucht wird → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Existierende Komponenten namentlich referenzieren („wie TotalAmountCard.tsx“) statt Design-Entscheidungen erneut in Prosa zu beschreiben, bewahrt System-Level-Konsistenz und reduziert Fehler → [[Lovable-Prototyp-dann-lokaler-Handoff]]
- Globale Komponenten (Navbar, Sidebar, Buttons) zuerst konsistent machen, bevor einzelne Seiten gebaut werden — jede neue Seite richtet sich dann automatisch daran aus → [[Lovable-Prototyp-dann-lokaler-Handoff]]
