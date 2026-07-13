---
url: keine
autor: "wiki-compiler / codex (vibe-repo, RAITEC AI Engineering OS)"
datum: 2026-04-16
erfasst: 2026-07-13
typ: artikel
---

# Wiki-Compiler zu „Vergleich von GSD, Superpowers, gstack und ECC – persönliche Learnings“

## Inhalt

Interner Wiki-Artikel aus `vibe-repo` (Pfad `docs/70_generated/wiki/03-methoden-und-tooling/04-vergleiche-und-einordnung/wka-vergleich-gsd-superpowers-gstack-ecc-persoenliche-learnings-2026-04-16.md`), ausdrücklich als persönlicher Erfahrungsbericht markiert, nicht als neutrale Marktübersicht.

Kernpunkte (kondensiert):

- Schwerpunkt-Unterscheidung: GSD → Dokumentation/Transparenz/Artefakte; Superpowers → Codequalität/TDD-Enforcement/Umsetzungsdisziplin; gstack → rollenbasierte Ausführung/Browser-QA/Shipping; ECC → Harness-Performance/Skill-Ökosystem/Memory/Security.
- Superpowers wird als „schwächer im Task-Tracking und weniger fein granularer Dokumentation“ eingeschätzt: statt vieler featurezentrierter Artefakte entstehen eher ein Design-Spec und ein Plan, die bei wachsendem Projekt unübersichtlich werden können. Passend für Solo-Founder/1-2-Personen-Teams, weniger für größere spec-getriebene Teams. Wichtige Gegenperspektive: Superpowers ist skill-basiert und damit anpassbar, wenn mehr Dokumentationstiefe gewünscht ist.
- GSD wird als stärker dokumentations-/transparenzorientiert eingeschätzt, mit `gsd-map-codebase` als besonders starkem Brownfield-Werkzeug (Tech-Stack, Architektur, Compliance, Konventionen, Risiken) und mehrperspektivischer Anforderungsprüfung (ein Agent erzeugt Requirements, ein zweiter prüft auf Lücken).
- gstack wird als stärker rollen-/command- als spec-getrieben eingeschätzt, mit Fokus auf Ausführung, QA und Browser-Arbeit statt Dokumentationsarchitektur.
- ECC wird als das breiteste und komplexeste System eingeschätzt (Skills, Commands, Hooks, Rules, Memory, Security, Continuous Learning), das eher eine ganze Agentenplattform als einen einzelnen Delivery-Flow bildet.
- Synthese: Der wichtigste Vergleichspunkt ist nicht „welches Framework ist besser“, sondern welches Problem gerade wichtiger ist (Dokumentationstiefe/Transparenz → GSD; schnelle disziplinierte Umsetzung → Superpowers; rollenbasierte Ausführung/QA → gstack; umfassende Agentenplattform → ECC).

## Kernaussagen

- Superpowers priorisiert schnelle, disziplinierte Solo-/Kleinteam-Umsetzung über feingranulare, featurezentrierte Dokumentation — eine bewusste Abwägung, keine Schwäche des Frameworks per se, weil es über Skills anpassbar bleibt → [[Workflow-Frameworks]]
- GSDs `gsd-map-codebase` und die mehrperspektivische Anforderungsprüfung (ein Agent erzeugt, ein zweiter prüft Requirements) sind konkrete Brownfield-Stärken → [[Workflow-Frameworks]]
- Die Wahl zwischen GSD/Superpowers/gstack/ECC sollte am dominanten Problem hängen (Dokumentationstiefe, Umsetzungsdisziplin, rollenbasierte QA-Ausführung, oder vollständige Agentenplattform), nicht an einer generellen Rangfolge → [[Workflow-Frameworks]]
