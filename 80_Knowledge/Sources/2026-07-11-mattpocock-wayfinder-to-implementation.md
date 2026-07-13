---
url: keine
autor: "@mattpocockuk (Matt Pocock)"
datum: 2026-07-11
erfasst: 2026-07-13
typ: tweet
---

# Matt Pocock zum Übergang von Wayfinder zur Implementierung

## Inhalt

One clarification for folks using /wayfinder:

The flow for big work should be:

/wayfinder -> /to-spec -> /to-tickets -> /implement

Once the /wayfinder map is complete, you turn it into a spec.

Some folks are using /wayfinder as the ENTIRE flow - from grilling to prototyping to shipped work

It certainly can be used that way - I've been doing that for non-coding stuff like course creation.

But for coding I much prefer creating a spec and handing off implementation to an AFK agent. Means I can focus on other things for a bit while it churns away.

## Kernaussagen

- Für große Coding-Vorhaben empfiehlt Matt Pocock den Fluss `/wayfinder → /to-spec → /to-tickets → /implement` → [[Task-basierte-Steuerung]], [[Plan-first-mit-getrenntem-Review]]
- Wayfinder klärt den Weg; nach Abschluss der Map wird sie für die Delivery in eine Spec und anschließend in Tickets überführt → [[Task-basierte-Steuerung]]
- Für nicht-codierende Arbeit kann Wayfinder den gesamten Prozess tragen; für Coding bevorzugt Matt eine getrennte AFK-Implementierungsphase → [[Klein-und-komposierbar]], [[Handoff-Doc]]
