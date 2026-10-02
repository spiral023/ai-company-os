---
url: https://github.com/latent-spaces/brag
autor: latent-spaces
datum: 2026-10-02
erfasst: 2026-10-02
typ: repo
thema: Tools & Releases
zeitkritisch: ja
---

# brag: `/brag` macht aus dem eigenen Projekt ein kurzes Launch-Video

Neu im Bestand: latent-spaces/brag. Laut `README.md` im Klon ist `/brag` ein Agent-Skill, der aus deinem Projekt ein kurzes Launch-Video mit Musik, Motion und Share-Texten erzeugt, gebaut auf Hyperframes. Der Ordner `skills/` enthält `brag` und `brag-slim`, `examples/` fünf Beispielprojekte. Gelesen, nichts ausgeführt.

## Kernaussagen
- Installation in Claude Code: `/plugin marketplace add latent-spaces/brag`, dann `/plugin install brag@brag`; danach `/brag` im Projekt. Andere Agenten: `npx skills add https://github.com/latent-spaces/brag --skill brag`.
- `/brag-slim` ist die schlanke Variante für Opus 5.5 ohne Hyperframes und ohne mitgelieferte Assets; unter Opus 5.5 schaltet `/brag` laut README automatisch darauf um, `/brag --full` erzwingt den klassischen Ablauf.
- Alternativ nennt die README den gehosteten Dienst letsbrag.app.

## Einordnung
Schnell gemachtes Marketing-Video für Side Projects. Wie gut die Ergebnisse sind, zeigt nur das Video selbst; im Repo gibt es dazu Beispiele, aber keine Messung.

## Verbindungen
- [[2026-10-01-julian-ivanov-ki-automat-claude-code-ist-unglaublich-gut-in-motion-graphi]]
