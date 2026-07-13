---
url: https://x.com/karpathy/status/2015883857489522876
autor: "Andrej Karpathy (@karpathy)"
datum: 2026-01-26
erfasst: 2026-07-13
typ: tweet
---

# Andrej Karpathy zu „Karpathys neuer Coding Workflow: 80% Agent, 20% Mensch“

## Inhalt

Karpathy wechselte innerhalb kurzer Zeit von 80% manuellem Coding (November) zu 80% Agent Coding (Dezember) — programmiert nun größtenteils in Englisch, beschreibt dem LLM „Code Actions“ in Worten.

Kernbeobachtungen: (1) IDEs bleiben nötig, wenn einem der Code wichtig ist — den Agenten „wie ein Falke“ beobachten. Neue Fehlerkategorie: Modelle machen keine Syntaxfehler mehr, sondern subtile konzeptionelle Fehler wie ein hastiger Junior Dev (Beispiel: Agent baut brüchiges 1000-Zeilen-Konstrukt, auf Nachfrage „geht das nicht einfacher?“ kürzt er auf 100 Zeilen — der Mensch muss Senior Engineer bleiben, der die Architektur prüft). (2) **Tenacity**: ein Agent wird nie müde oder demoralisiert — 30 Minuten an einem Problem kämpfen, wo ein Mensch aufgegeben hätte, und am Ende gewinnen. (3) Haupteffekt ist nicht Geschwindigkeit, sondern **Expansion**: Dinge werden gebaut, die sich vorher nicht gelohnt hätten (ROI zu niedrig) oder die mangels eigener Skills nie angefasst worden wären. (4) **Leverage**: Imperativ zu Deklarativ wandeln — nicht sagen was zu tun ist, sondern Success Criteria geben; testgetrieben arbeiten lassen (Tests schreiben lassen, dann bestehen lassen); Optimization Loop (erst naiven korrekten Algorithmus, dann unter Korrektheitserhalt optimieren lassen). (5) Programmieren fühlt sich spaßiger an (Fleißarbeit entfällt), aber die Fähigkeit, manuell Code zu schreiben, verkümmert („Atrophy“). Zentrale Erkenntnis: **„Generation“ (Schreiben) und „Discrimination“ (Lesen/Reviewen) sind unterschiedliche Fähigkeiten** — man kann weiterhin reviewen, auch wenn man Schwierigkeiten hat, den Code selbst syntax-perfekt zu schreiben. (6) Erwartet für 2026 eine Flut von minderwertigem AI-Content („Slopacolypse“) parallel zu echten Produktivitätsgewinnen.

## Kernaussagen

- Neue Fehlerklasse bei Agentencoding: keine Syntaxfehler mehr, sondern subtile konzeptionelle Fehler und Überkomplizierung (Bloat) — der Mensch bleibt in der Rolle des Senior Engineers, der Architektur hinterfragt → [[Great-Decoupling-Rollenverstaendnis]]
- „Generation“ und „Discrimination“ sind unterschiedliche Fähigkeiten: Code-Review-Kompetenz bleibt auch dann erhalten, wenn die Fähigkeit zum manuellen Schreiben durch Nichtnutzung verkümmert → [[Great-Decoupling-Rollenverstaendnis]]
- Leverage entsteht durch Deklarativ-statt-Imperativ (Success Criteria statt Anweisungen), testgetriebenes Arbeiten und einen Optimization-Loop (erst korrekt, dann unter Korrektheitserhalt optimieren) → [[Great-Decoupling-Rollenverstaendnis]], [[TDD-als-Verifikationshebel]]
