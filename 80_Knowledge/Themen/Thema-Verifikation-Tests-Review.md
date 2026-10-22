# Verifikation, Tests & Review

*Automatisch erzeugt von `70_Scripts/themen.py index` am 2026-10-22. Nicht von Hand ändern: Taxonomie in `themen.yaml`, Zuordnung in `zuordnung.yaml`.*

Wie Menschen und Coding Agents gemeinsam Codequalität sichern: TDD, Testharness, Mutation Testing, statische Analyse, Quality Gates und getrennte Autor-/Prüfkontexte. Dazu gehören risikobasiertes Human Review, menschliche Verantwortung und Freigaben (Human in the Loop), Review-Kapazität sowie PR-Größe und Aufteilung in überschaubare Änderungen. Agent-Autonomie gehört hier hinein, soweit sie Prüf- und Freigabeentscheidungen betrifft; autonome Ausführung steht in autonomie, der gesamte Entwicklungsprozess in sdlc.

## Suchbegriffe

- **Hauptkeyword:** AI Code Review
- **Long-Tail:** TDD mit Coding Agents; Testharness für Agents; Mutation Testing KI; Reward Hacking Tests; Adversarial Review Agent; Review als Engpass; Codequalität mit KI und Menschen; Human in the Loop beim Code Review; Risikobasiertes Human Review; Agent-Autonomie und menschliche Freigaben; Große KI-generierte PRs prüfen; Pull Requests in prüfbare Änderungen aufteilen; Review-Kapazität bei parallelen Agents
- **Fragen:** Wie prüfe ich KI-generierten Code? / Warum schreibt der Agent Tests passend zum Bug? / Welche Änderungen brauchen menschliches Review und welche automatische Checks? / Wer trägt die Verantwortung, wenn ein Agent Code freigibt? / Was tun, wenn PRs zu groß für ein gründliches manuelles Review werden? / Wie begrenzt Review-Kapazität die Agent-Autonomie und Parallelisierung?
- **Häufig in den Quellen:** test (14), review (13), testharness (12), tests (8), tdd (8), qualität (5), verifikation (5), human-in-the-loop (5), menschliche freigabe (4), risikobasiertes human review (4), verhaltensvergleich (4), mutation testing (4), refactoring (4), skill (4), gstack (4), rea (4), reverse engineering (4), pre-commit hooks (3), deep modules (3), /goal (3)

## Verwandte Themen

- [[Thema-Spezifikation-Planung]] — Spezifikation & Planung
- [[Thema-Autonome-Läufe-Loops-CI]] — Autonome Läufe, Loops & CI
- [[Thema-Multi-Agent-Parallelisierung]] — Multi-Agent & Parallelisierung
- [[Thema-Skill-Design]] — Skill-Design
- [[Thema-AI-nativer-SDLC]] — AI-nativer SDLC
- [[Thema-Sicherheit-Sandboxing]] — Sicherheit & Sandboxing
- [[Thema-Rolle-Lernen-Markt]] — Rolle, Lernen & Markt

## Patterns (19)

- [[Abstraktionswert-mit-Deletion-Test-pruefen]] · verifiziert · 2 Belege
- [[Domaenen-Harness-mit-Daten-Evals-Rechten-und-Review]] · meinung · 1 Belege
- [[Externe-Evaluatoren-mit-dauerhaftem-Zugang]] · meinung · 1 Belege
- [[Fachregel-Konsolidierung-vor-Featureaenderung]] · meinung · 2 Belege
- [[Framework-Quellcode-als-idiomatische-Referenz]] · meinung · 2 Belege
- [[Helper-Nutzung-durch-Lint-erzwingen]] · meinung · 6 Belege
- [[Hillclimbing-mit-Holdout-Split]] · meinung · 4 Belege
- [[Menschliche-Aufsicht-als-eigene-Leistung-pruefen]] · meinung · 1 Belege
- [[Mutationstests-fuer-Agent-geschriebene-Tests]] · meinung · 1 Belege
- [[Produktreife-durch-echte-Testnutzer]] · meinung · 2 Belege
- [[Pruefungen-nach-Feedbackzeitpunkt-staffeln]] · meinung · 1 Belege
- [[Refactoring-mit-Verhaltensvergleich]] · meinung · 4 Belege
- [[Review-Autonomie-mit-Shadow-Mode-und-Stichproben]] · meinung · 7 Belege
- [[Schema-als-Vertrag-mit-generierten-Clients]] · meinung · 2 Belege
- [[TDD-als-Verifikationshebel]] · mehrfach-belegt · 14 Belege
- [[Testharness-als-staerkster-Hebel]] · meinung · 60 Belege
- [[UI-Grenzfaelle-mit-realistischen-Daten-pruefen]] · verifiziert · 3 Belege
- [[Visuelle-Abnahme-mit-Live-Lokal-Vergleich]] · meinung · 10 Belege
- [[Zustandslose-CI-Listener-mit-Ergebnisjournal]] · meinung · 1 Belege

Weitere Patterns mit diesem Thema als Nebenthema: [[Adversarialer-Pre-Launch-Check]], [[Agent-Tracing-nach-Beobachtungsebene]], [[Ambitionscheck-mit-Zielhoehe-Tiefe-und-Reichweite]], [[Anti-Rationalization-Tables]], [[CI-Agent-mit-Review-Gate]], [[Decision-Head-Finetuning]], [[Framebasierte-Motion-Produktion-mit-Brief-und-Abnahme]], [[Great-Decoupling-Rollenverstaendnis]], [[KI-Adoption-mit-Use-Case-und-Befaehigungs-Gate]], [[Kontrollierte-Agent-Parallelisierung]], [[Lokale-Inferenz-nach-Arbeitslast-dimensionieren]], [[Plan-first-mit-getrenntem-Review]], [[Produktwert-jenseits-des-reproduzierbaren-Codes]], [[Quellen-Bookmarks-fuer-Agent-Automationen]], [[RAG-mit-Text-Tabellen-und-Volltextpfad]], [[Skill-Qualitaet-durch-Trigger-und-Baseline-Evals]], [[Suchintention-mit-Daten-vor-Webdesign-klaeren]], [[Variantenvergleich-vor-Produktionsabnahme]], [[Videoanalyse-mit-Frames-und-Transkript]]

## Quellen (51)

- [[2026-10-21-mattpocockuk-2112880319934165307]] — Matt Pocock empfiehlt eine Lernfolge von persönlicher über interne zu öffentlich zugänglicher Software.
- [[2026-10-19-voxyz_ai-2112302775547679169]] — Vox beschreibt vier Agent-Perspektiven für den Weg von der Landingpage zum ersten Produkterfolg.
- [[2026-10-18-floknowsai-ria-ist-aktuell-der-gehypteste-ki-skill-macht-deine-ki-agenten-zu]] — Florian beschreibt `REA` als Workflow zum Untersuchen, Verstehen und anschließenden eigenen Umsetzen bestehender Software.
- [[2026-10-17-voxyz_ai-2111442102756463077]] — Vox bündelt 23 Prüfideen vor der ersten Zahlung einer agentengestützt gebauten App.
- [[2026-10-17-developers-maintaining-software-with-the-gpt-6-family-opena]] — OpenAIs Core-Experimentation-Team beschreibt, wie Coding-Agenten Wartungskandidaten finden, Produktionsbelege sammeln und kleine Änderungen zur Prüfung vorbereiten.
- [[2026-10-16-poteto-2111133080526495985]] — Lauren schlägt vor, wiederkehrende Agentkorrekturen möglichst in der Codebasis zu verankern: Architektur vor automatischen Checks, knapper Prosa und gezieltem menschlichem Review.
- [[2026-10-16-math_rachel-2111238648188584306]] — Rachel Thomas diskutiert einen Fachbeitrag zur menschlichen Aufsicht über KI-Agenten.
- [[2026-10-15-vincentmumme-greg-isenberg-ist-wahrscheinlich-aktuell-einer-der-wichtigsten]] — Vincent Mumme ordnet Greg Isenbergs Marktbeobachtungen ein.
- [[2026-10-15-claude-how-the-claude-code-team-does-code-review-claude]] — Addy Osmani beschreibt den internen Review-Prozess des Claude-Code-Teams: Maschinen übernehmen wiederholbare Fehlersuche, Menschen beurteilen Absicht, Architektur, Risiko und verbleibende Prüflücken.
- [[2026-10-14-matt-pocock-mutation-testing-is-awesome]] — Matt Pocock stellt am 14.
- [[2026-10-13-mattpocockuk-2109973273924579720]] — Matt Pocock nennt typische Reibungsverluste: überhöhten Effort, lange Skills, aufgeblähte globale Regeln und fehlende Selbstprüfung.
- [[2026-10-13-matt-pocock-stop-running-your-checks-in-harness-hooks]] — Matt Pocock empfiehlt am 13.
- [[2026-10-12-sarahfim-2109736893198016898]] — Sarah beschreibt aus ihrer Rolle als Product-Engineering-Leiterin bei Composio, wie Repositorystruktur und automatisierte Prüfungen Beiträge verschiedener Agenten beherrschbar machen sollen.
- [[2026-10-12-0xmovez-2109604520770548146]] — Movez beschreibt einen Workflow, in dem `Opus 5.5` über REA spezialisierte Analysewerkzeuge bedient und Erkenntnisse schrittweise in eine Spezifikation und Reimplementierung überführt.
- [[2026-10-12-0xcodila-2109623431763292649]] — Der übertragbare Kern von Codilas REA-Kurs ist die Kette Untersuchung → Verhaltensspezifikation → eigene Implementierung → Vergleichstest.
- [[2026-10-11-shiptypes-ship-types-not-docs]] — Der Beitrag auf Ship types schlägt vor, maschinenlesbare Schemas als gemeinsamen Vertrag zwischen Services, Clients und Coding Agents zu pflegen.
- [[2026-10-10-voxyz_ai-2109026189298012522]] — Vox beschreibt am `2026-10-10` ein als offiziell bezeichnetes Game-Studio-Plugin für Codex mit neun Skills.
- [[2026-10-09-openai-refactoring]] — Kleine Refactoring-Schritte erhalten öffentliche Schnittstellen und werden am vereinbarten Verhalten geprüft.
- [[2026-10-08-moritz-brandes-sauberer-code-mit-claude-code-so-geht-s-wirklich]] — Lokal lesbarer Framework-Code ergänzt idiomatische Referenzen; Versionspassung, gezielte Lesegrenzen und eigene Verhaltenstests bleiben Übernahmebedingungen.
- [[2026-10-06-voxyz_ai-2107576635578855461]] — Vox schlägt eine Regel für `Claude Code` vor: Nach visuellen Codeänderungen prüft ein Subagent mit `codex-cu` die betroffenen Seiten im bereits freigegebenen Browser.
- [[2026-10-05-venelin-valkov-stop-ai-code-slop-yes-you-still-need-to-refactor]] — Refactoring erhält konkrete Mess- und Verhaltensprüfungen; Renderzählungen einzelner Komponenten belegen keine vollständige Gleichheit oder schnellere Gesamtlaufzeit.
- [[2026-10-05-repo-millionco-react-doctor-skill]] — Im Klon von millionco/react-doctor (Stand Commit `1b149bae`) liegt der Agent-Skill `skills/react-doctor/SKILL.md` (Version 1.2.0).
- [[2026-10-05-repo-mattpocock-skills-retro]] — Im Klon von mattpocock/skills (Stand Commit `4588b32`, Version 1.3.1) liegt `retro` unter `skills/engineering/retro/SKILL.md`.
- [[2026-10-04-voxyz_ai-2106829206134931539]] — Vox empfiehlt, wiederholte Agentkorrekturen in fertige Funktionen oder Typen zu überführen und alternative Implementierungen mit `Lint` zu verbieten.
- [[2026-10-02-voxyz_ai-2106104334035435572]] — Vox empfiehlt, vor Änderungen sämtliche Implementierungen der betroffenen Regel zu kartieren: Dateien, Kopien und Ergebnisse für identische Eingaben.
- [[2026-10-02-repo-thedaviddias-front-end-checklist]] — Im Klon von thedaviddias/Front-End-Checklist (Stand Commit `7bfd8680`) beschreibt `packages/cli/README.md` die CLI `@frontendchecklist/cli`; die Regeln liegen im Paket, sie läuft offline.
- [[2026-10-02-repo-garrytan-gstack]] — Laut `CHANGELOG.md` von garrytan/gstack (Repo-Stand Commit `7fca42ad`, Einträge um v1.91.9.0) wenden alle Workflows, die Tests vorschlagen, schreiben, prüfen oder ausliefern, eine gemeinsame „Test Val
- [[2026-10-01-mattpocockuk-2105563604384915639]] — Pocock schlägt vor, mit `/codebase-design` nach Shallow Modules zu suchen und den **Deletion Test** auf mögliche Entfernungskandidaten anzuwenden.
- [[2026-09-28-claude-automating-eval-design-and-hillclimbing-with-cla]] — Anthropic beschreibt Prinzipien für Eval-Design und für das schrittweise Verbessern gegen ein Eval (Hillclimbing) und zeigt, wie die Befehle `/claude-api build-eval` und `/claude-api hillclimb` im `cl
- [[2026-09-24-ai-engineer-matt-pocock-fixing-the-pr-bottleneck]] — Mehr Agent-Output verschärft den Review-Flaschenhals: deterministische Checks, ein separater Review-Agent mit Commits und risikobasiertes Human Review bremsen ihn in drei Stufen.
- [[2026-09-14-voxyz_ai-2099528601557496220]] — Vox empfiehlt konkrete Handlungen und erwartete Ergebnisse für die Abnahme durch Agenten.
- [[2026-09-14-claude-agentic-coding-is-straining-ci-here-s-how-we-sca]] — Sachin Malhotra beschreibt, wie Anthropic seine Test-Impact-Analyse nach mehreren kurzlebigen Patches neu aufbaute.
- [[2026-08-25-vikingmute-2092059170812108811]] — Ein strenger Review-Skill sucht zuerst Vereinfachungen der Struktur statt Detailkritik, erzeugt aber bei Bestandscode schnell mehr Befunde, als sich abarbeiten lassen.
- [[2026-08-19-matt-pocock-live-uncle-bob-on-software-fundamentals-in-the-a]] — Statt langer Regeltexte gehören deterministische Tools wie Mutation Testing und Komplexitätsmetriken in eine Agent-Schleife, weil Modelle lange Regeldokumente nur als Richtlinie behandeln.
- [[2026-08-18-floknowsai-hoer-auf-den-code-deines-ki-agenten-zu-lesen]] — Autor und Prüfer müssen getrennt sein: Mutation Testing prüft die Tests selbst, ein zweiter Agent mit frischem Kontext bewertet Code und Testqualität.
- [[2026-08-14-mattpocockuk-2088256432265167185]] — Matt Pocock beschreibt einen kurzen Lernkreislauf: unerwünschtes Agent-Verhalten beobachten, eine konkrete Regel in `CODING_STANDARDS.md` im Repo-Root festhalten und `/code-review` diese Regel beim Re
- [[2026-08-14-floknowsai-ueber-achtzig-prozent-des-codes-von-claude-code-und-codex-sieht-kein]] — Ein Agent findet eigene Fehler seltener im selben Verlauf, weshalb eine frische Prüf-Session mit gleich starkem Modell und erzwungenen Status-Checks besser verifiziert.
- [[2026-08-05-creatoreconomy-use-my-human-review-skill-to-edit-html-and-markd]] — Feedback direkt an der Stelle in der Datei ist präziser als Chat-Anweisungen und verhindert, dass ungeprüfte Agent-Edits Slop ins Projekt tragen.
- [[2026-08-04-anthropic-docs-claude-code-best-practices]] — Anthropic empfiehlt Verifikation als vierstufige Eskalation vom Prompt über Goal-Evaluator und Stop-Hook bis zur zweiten Meinung durch ein frisches Modell, ergänzt um Plan-first und Session-Hygiene.
- [[2026-08-02-promptgefluester-wenn-ihr-versucht-euer-software-projekt-mit-fable-five-oder-o-plus-5]] — Vor einem KI-Refactoring deterministische statische Analyse laufen lassen, toten Code entfernen und Architekturregeln festlegen, statt das Modell Abhängigkeiten selbst abgleichen zu lassen.
- [[2026-07-26-promptgefluester-ich-hab-ne-unbequeme-wahrheit-und-zwar-ich-wurde-gefragt-wieso]] — Bei größeren Codebasen liefern dichte deterministische Prüfungen die Qualität, nicht das Modell allein, und kosten bewusst Zeit und Pflege.
- [[2026-07-23-unclebobmartin-2080257779395154409]] — Robert C.
- [[2026-07-23-colebemis-2080392348836790395]] — Cole Bemis empfiehlt, den Coding Agent annotierte Screenshots an einen Pull Request anhängen zu lassen.
- [[2026-07-21-claudedevs-2079654423828304282]] — Anthropic beschreibt Sprachmigrationen anhand eines Zig-zu-Rust-Ports von Bun und eines Python-zu-TypeScript-Ports eines internen Werkzeugs.
- [[2026-07-16-matt-pocock-do-software-fundamentals-still-matter]] — Matt Pocock begründet am 16.
- [[2026-07-16-amasad-2077802290304684404]] — Replit-CEO Amjad Masad beschreibt, wie Replit zwischen Januar und Juni 2026 interne Agents in Engineering, Data, Sales, Marketing und Support eingeführt hat.
- [[2026-07-01-0xcodila-2072329149520232639]] — Der X-Artikel erklärt Loops als Ziel, auf das ein Agent ohne Prompt pro Schritt hinarbeitet, und stützt sich auf Karpathys `autoresearch` und eine Bilevel-Arbeit.
- [[2026-02-14-matt-pocock-skill-tdd-claude-code]] — Ein Test, eine Implementierung, wiederholen: Vertikale Tracer-Bullet-Zyklen verhindern, dass das Modell Tests umschreibt oder nur Mocks verifiziert.
- [[2026-02-04-tweag-tdd-agentic-coding]] — Ein Test ist ein präziser Prompt: Der Agent baut Logik Test für Test, wobei die Testqualität beim Menschen liegt.
- [[2026-01-12-dhruv1103-lessons-learned-500k-lines-claude-code]] — Modulare Architektur, TDD gegen echte Container, Read-only-MCP-Diagnose und gründliches Review machen große KI-Codebasen beherrschbar.
- [[2025-06-28-the-morpheus-tutorials-ai-ersetzt-uns-itler-jetzt-also]] — Issues, Codepfadprüfung, Implementierung, Review und manuelle Ausführung bilden einen beschriebenen Entwicklungsablauf; Arbeitsmarktprognosen bleiben unbestätigt.

## Quellen mit diesem Thema als Nebenthema

- [[2026-10-22-cursor-pstack-engineering-skills]]
- [[2026-10-20-artificialanlys-2112582116651466965]]
- [[2026-10-17-nutzerquelle-motion-video-qualitaetskriterien]]
- [[2026-10-17-kimmonismus-2111385805449048181]]
- [[2026-10-17-julian-ivanov-ki-automat-motion-graphics-mit-ki-bildern-kombinieren-in-cl]]
- [[2026-10-16-voxyz_ai-2111079716832886886]]
- [[2026-10-16-artificialanlys-2111052531166249039]]
- [[2026-10-15-mardehaym-2110763129885835505]]
- [[2026-10-14-promptgefluester-rea-reverse-engine-anything-im-augenblick-auf-github-trending-mit-239]]
- [[2026-10-14-poteto-2110496830429839869]]
- [[2026-10-13-matt-pocock-tell-your-agents-to-care-about-the-codebase]]
- [[2026-10-13-felixrieseberg-how-to-be-more-ambitious-a-tutorial-for-humans-w]]
- [[2026-10-13-anthropic-redesigning-source-control-at-anthropic]]
- [[2026-10-13-alex-sprogis-so-nutzt-du-rea-um-jede-app-in-minuten-zu-kopier]]
- [[2026-10-12-promptgefluester-warum-meiner-meinung-nach-software-service-und-aeh-plattformen-mit-ki]]
- [[2026-10-12-julian-ivanov-ki-automat-ki-kopiert-jetzt-jede-software-und-keiner-kann-e]]
- [[2026-10-12-josharosen-2109649928276341191]]
- [[2026-10-11-hood-informatik-wird-code-jetzt-wertlos]]
- [[2026-10-10-voxyz_ai-2108875199164871053]]
- [[2026-10-10-boristane-self-improving-software-is-inevitable]]
- [[2026-10-09-voxyz_ai-2108573215224160393]]
- [[2026-10-09-voxyz_ai-2108543002830360775]]
- [[2026-10-09-satyanadella-2108627923888754862]]
- [[2026-10-09-repo-superpowers-workflow]]
- [[2026-10-09-repo-gstack-workflow]]
- [[2026-10-09-julian-ivanov-ki-automat-websites-mit-ki-bauen-die-gut-aussehen-und-perfo]]
- [[2026-10-09-beamnxw-2108616740846420354]]
- [[2026-10-08-voxyz_ai-2108324058739745228]]
- [[2026-10-08-heise-dekompilierung-per-ki-warum-closed-source-laut-r]]
- [[2026-10-07-unslothai-decision-model-finetuning]]
- [[2026-10-05-repo-garrytan-gstack-retro]]
- [[2026-10-05-repo-bmad-method-retrospective]]
- [[2026-10-05-repo-alirezarezvani-skill-doctor]]
- [[2026-10-05-aihero-v1-3-implement-spec-pr-retro-and-glossary-md]]
- [[2026-10-04-voxyz_ai-2106783910055006342]]
- [[2026-10-04-promptgefluester-ich-zeig-ja-grade-wie-ich-ueber-280-webseiten-in-den-naechsten-paar]]
- [[2026-10-04-emilkowalski-2106752670405099523]]
- [[2026-10-03-vincentmumme-andrej-karpathy-einer-der-fuehrenden-ki-forscher-erfinder-vom-llm-wiki]]
- [[2026-10-02-voxyz_ai-2106006290954592332]]
- [[2026-10-02-seeconvm-2106096193235259564]]
- [[2026-10-01-floknowsai-diese-faehigkeiten-helfen-dir-2026-bei-deiner-arbeit-mit-ki-damit-du]]
- [[2026-10-01-0xwhrrari-2105643919119696297]]
- [[2026-09-30-flxrnc-2105311836190978392]]
- [[2026-09-27-voxyz_ai-2104224555040452925]]
- [[2026-09-27-anthropic-academy-sdlc-playbook]]
- [[2026-09-26-ai-mit-arnie-gpt-6-kann-endlich-design]]
- [[2026-09-25-voxyz_ai-2103586663393853636]]
- [[2026-09-25-trq212-2103576349499855160]]
- [[2026-09-25-promptgefluester-weil-mich-viele-danach-gefragt-haben-wollt-ich-jetzt-kurz-noch-n]]
- [[2026-09-24-mattpocock-ai-coding-dictionary]]
- [[2026-09-20-eric-tech-claude-code-the-complete-ai-native-sdlc-guide]]
- [[2026-09-15-emilkowalski-2099948779864793303]]
- [[2026-09-14-shadcn-2099534231114314145]]
- [[2026-09-14-code-test-plugins-with-evals-claude-code-docs]]
- [[2026-09-12-darioamodei-2098773920774074715]]
- [[2026-09-10-promptgefluester-einer-der-groessten-fehler-den-ich-bei-vielen-vibe-codern-mit-ki]]
- [[2026-09-01-ai-mit-arnie-lokale-ki-kauf-nicht-die-falsche-hardware]]
- [[2026-08-30-alex-sprogis-loop-graph-engineering-das-letzte-video-was-du-s]]
- [[2026-08-28-the-morpheus-der-huggingface-hack-ist-jetzt-untersucht]]
- [[2026-08-19-developer-evaluating-ai-agent-skill-performance-with-nvidi]]
- [[2026-08-12-kimmonismus-2087452378299564147]]
- [[2026-08-09-julian-ivanov-ki-automat-5-claude-code-skills-die-dir-wirklich-arbeit-abn]]
- [[2026-08-05-floknowsai-dein-vibe-coding-projekt-bricht-nicht-am-coding-agent-zusammen-sondern]]
- [[2026-07-30-matt-pocock-wayfinder-nothing-is-too-big-to-plan-anymore]]
- [[2026-07-24-agenticjames-the-creator-of-claude-code-released-a-guide-to-the-4-levels-of-ai-coding]]
- [[2026-07-21-claude-how-anthropic-secures-its-ai-native-software-dev]]
- [[2026-07-20-matt-pocock-do-you-even-need-human-review]]
- [[2026-07-16-matt-pocock-mattpocock-skills-a-complete-ai-coding-workflow]]
- [[2026-07-13-matt-pocock-live-the-wayfinder-demo]]
- [[2026-07-06-claudedevs-2074208949205881033]]
- [[2026-06-10-ai-news-strategy-daily-n-codex-vs-claude-code-stop-picking-one-here-s-wha]]
- [[2026-06-07-julian-ivanov-ki-automat-so-laesst-du-claude-jedes-video-fuer-dich-anscha]]
- [[2026-04-16-wiki-compiler-gstack]]
- [[2026-04-13-alex-sprogis-superkraefte-fuer-claude-code]]
- [[2026-04-10-paulsolt-2042716870512353294]]
- [[2026-03-26-alex-sprogis-gsd-framework-fuer-claude-code-version-1-2-im-pr]]
- [[2026-02-23-d4m1n-ralph-loop-setup-primaer]]
- [[2026-02-19-lenny-s-podcast-head-of-claude-code-what-happens-after-coding-is]]
- [[2026-02-13-vincanger-claude-code-fullstack-essentials]]
- [[2026-02-05-carlini-anthropic-c-compiler]]
- [[2026-02-03-svpino-claude-code-md-tips]]
- [[2026-01-26-karpathy-coding-workflow-2026]]
- [[2026-01-20-mrexodia-vibe-engineering]]
- [[2026-01-04-ai-news-strategy-daily-n-why-andrej-karpathy-feels-behind-and-what-it-mea]]
- [[2025-12-06-the-morpheus-tutorials-software-entwickeln-mit-ki-einsteiger-guide]]
- [[2025-12-04-brutkasten-business-vs-technik-wie-man-ki-in-organisationen]]
- [[2025-09-22-julian-ivanov-ki-automat-das-ultimative-rag-system-n8n-nextcloud-mistral]]
- [[2025-09-08-the-morpheus-tutorials-studien-ai-verdraengt-also-junior-itler]]
- [[2025-04-09-the-morpheus-ki-ist-ein-segen]]
