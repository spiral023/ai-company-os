---
url: https://www.youtube.com/watch?v=cKgbU_wWWts
titel: "Die Qualität von KI-Code ist nicht so gut wie du denkst.."
autor: "Alex Sprogis"
datum: 2026-10-25
erfasst: 2026-10-28
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-28
source_notiz: 80_Knowledge/Sources/2026-10-25-alex-sprogis-die-qualitaet-von-ki-code-ist-nicht-so-gut-wie-d.md
video_id: "cKgbU_wWWts"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "431"
---

# Die Qualität von KI-Code ist nicht so gut wie du denkst..

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=cKgbU_wWWts](https://www.youtube.com/watch?v=cKgbU_wWWts)

## Videobeschreibung

📌 Links:
Digitale Leute Summit 2026: https://link.alexsprogis.de/dl-summit
Nutz den Code "DLS26ALEX15" für 15% Rabatt auf deine Tickets

Mein kostenloser AI Engineering BLUEPRINT: https://link.alexsprogis.de/CYSUlx

Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/18hX7N

Does Code Quality even matter? (Max Kanat-Alexander): https://www.youtube.com/watch?v=bU5gDVyu_28

State of Code 2026 Report: https://www.sonarsource.com/state-of-code-developer-survey-report.pdf

Sonar Opus 5.5 Review: https://www.sonarsource.com/blog/claude-opus-5-5-an-evaluation/
Veracode Code Security Report: https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk/

Endorlabs Analyse: https://www.endorlabs.com/learn/opus-5-5-6x-cheaper-and-2x-faster-than-fable-5-1-but-memorization-keeps-it-off-the-top-spot


Ist Code-Qualität noch wichtig, wenn Claude Code, Codex und Co. den Code schreiben? Die einen sagen, die Modelle sind inzwischen gut genug. Die anderen sagen, ohne strukturiertes System baust du auf Sand. In diesem Video schauen wir uns an, wer recht hat.

Du erfährst, warum Code-Qualität überhaupt wichtig ist und was aktuelle Analysen aus 2026 über den Code von Opus 5.5, Codex und Co. sagen. Außerdem geht's darum, wann Code-Qualität bei Wegwerf-Software egal ist und wann nicht. Mit vier Fragen kannst du einschätzen, wie viel Sorgfalt dein eigenes Projekt braucht. Und ich zeige dir, wie ich mit Spezifikationen, Tests, einem unabhängigen Prüf-Agent und strengen automatischen Checks dafür sorge, dass Qualität mich kaum zusätzlichen Aufwand kostet.
----

Kapitel:

00:00 Intro
01:11 Warum ist Code-Qualität wichtig?
04:15 Wie gut ist der Code von Claude Code, Codex & Co.?
06:11 Wegwerf-Software
07:09 Qualität in deinem Projekt
08:00 Digitale Leute Summit
09:03 So wird Qualität billig

----


🛠 Mein Tech Stack:
Editor: VS Code (kostenloser Code Editor)
Coding Agent: Claude Code (Opus 4.7)
Frontend: Next.js / Tailwind
Backend: Supabase
Deployment: Hostinger* (https://www.hostg.xyz/SHJ1Z)
Verwende "ALEXSPROGIS" für 10% Rabatt auf Jahrespläne.

-----
🔔 Abonnier den Kanal  um kein weiteres Video zu verpassen
-----
📱 Folge mir auch auf anderen Kanälen:
LinkedIn: https://www.linkedin.com/in/alexander-sprogis/
Instagram: https://www.instagram.com/alex.sprogis/
TikTok: https://www.tiktok.com/@alexsprogis
-----

Auf diesem Kanal bekommst du:
- Updates zu den neuesten KI-Tools für Produktentwicklung mit AI
- Best Practices zu AI-Tools wie Claude, Cursor, Supabase und co.
- Schritt-für-Schritt-Workflows zum Nachbauen
- Einfache Erklärungen, die komplexe KI-Konzepte - verständlich für jeden

Über mich:
Ich bin Alex. Nach 10 Jahren im Produktmanagement und 4,5 Jahren als Agency-Founder (VisualMakers) zeige ich dir hier, wie du sichere und skalierbare Software mit AI baust, auch ohne Vorkenntnisse.

Mehr zu mir findest du auf https://alexsprogis.de

## Transkript

Ist Code Qualität eigentlich noch wichtig, wenn KI den Code schreibt oder kümmert sich die KI da mittlerweile selber drum? Wenn ich mir das so anschaue, dann gibt's gerade zwei Lager. Die einen sagen, die Modelle sind inzwischen so gut, selbst wenn du einfach nur drauf los promptest, musst du dir eigentlich gar nicht mehr anschauen, was da im Hintergrund überhaupt produziert wird. Und zur Not setzt du irgendwie noch einen zweiten Agent drauf an, der das Ganze am Ende prüft und dann passt das schon. Und andere sagen wiederum, Coding Agents haben noch massive Probleme, ja? Sie betreiben Overengineering, sie entwickeln viel zu komplex, nehmen Abkürzungen, reden sich Ergebnisse schön, drehen sich in Fehlerschleifen und vergessen immer wieder Dinge. Und ohne strukturiertes System baut man quasi nur auf Sand. Die Frage interessiert natürlich vor allem neue Leute, die gerade anfangen, Lösungen mit Coding Agents zu bauen, die aber gar keinen Engineering Hintergrund haben.

Denn die beschäftigt natürlich, ob sie sich auf das, was der Agent überhaupt produziert, auch verlassen können. Was ich dir schon sagen kann, es ist natürlich eine es kommt darauf an Frage. Aber worauf genau kommt es denn an? Das will ich mit dir in diesem Video einmal durchgehen, sodass du am Ende auch abschätzen kannst, wie viel Qualität dein eigenes Projekt eigentlich braucht und wie du diese Qualität mit Claude, Codex und Co. bekommst. Der Rahmen für das Video stammt aus einem Talk von einem Autor und Software Engineer Max Kennet Alexander von Capital One. Falls du dir den Talk anschauen willst, den habe ich dir natürlich in der Videobeschreibung verlinkt. Bevor wir uns die Frage stellen, ob Claude, Codex und Co. überhaupt eine gute Qualität liefern und ob das überhaupt noch wichtig ist, will ich erstmal die Frage beantworten, warum war Coding Qualität überhaupt jemals wichtig? Weil sich gut strukturierter, sauberer Code gut anfühlt, reicht leider nicht als Antwort alleine. Denn alles, was du mit Software erreichen willst, hängt im Prinzip an zwei Dingen. Erstens, du musst dein System verstehen. Und zweitens, musst du auf Basis dieses Verständnisses handeln können. Qualitätswerkzeuge wie Tests, Debugger, Monitoring, all das gibt es im Grunde nur für diese zwei Dinge.

Verstehen heißt dabei ganz konkret zwei Fragen. Und zwar einmal, was macht mein System tatsächlich, wenn es läuft, also unabhängig von irgendwelcher Dokumentation, die irgendwo steht, und wie mache ich Änderungen am System, ohne irgendwas dabei kaputt zu machen? Wenn du dir jetzt irgendwie eine kleine Helfer App gebaut hast dich persönlich, dann ist das absolut trivial. Aber bei einer echten, produktiven App, die ja über Jahre gewachsen ist, kann irgendwann niemand mehr die ganze Anwendung im Kopf behalten. Das wiederum heißt, du brauchst eine Struktur, in der sich diese große Applikation als Ganzes auf einzelne Bausteine zurückführen lässt. Und Begriffe wie Lesbarkeit und Testbarkeit bedeuten im Kern eben genau das, nämlich eine verständliche Struktur. Und das wird vor allem dann wichtig, wenn du etwas an deiner Anwendung ändern möchtest. Denn jede Änderung hat zwei Risiken. Erstes Risiko, du verursachst mit deiner Änderung ein Problem. Problem kann in dem Fall heißen, es entsteht dadurch ein tatsächlicher Bug oder die Implementierung dauert dreimal so lange wie geplant oder es entsteht irgendein Verhalten, das du nicht wolltest oder das Budget für die Umsetzung ist z.B. komplett aus dem Ruder gelaufen. Und zweites Risiko, du machst das System schwerer zu verstehen und damit auch zu warten. Und daraus resultiert dann, dass jede zukünftige Änderung immer riskanter wird, weil du dadurch zunehmend technische Schulden aufbaust. Die beiden stehen jetzt in direkter Korrelation zueinander, denn Punkt 2 füttert quasi Punkt 1. Je schwerer dein System zu verstehen ist, desto mehr Probleme verursachst du und die machen es wiederum noch schwerer, das Ganze wieder zu verstehen. Das schaukelt sich dann so lange hoch, bis irgendwann der Punkt kommt, an dem jede Änderung ein Problem verursacht. Die beste Analogie ist quasi das Kabelmanagement unter meinem Schreibtisch. Ich habe da zwei große Steckdosenleisten und sobald ich die ersten beiden Geräte eingesteckt habe, dann ist das alles noch übersichtlich, ja, ich weiß ganz genau, welcher Stecker welchem Gerät zugeordnet ist. Vielleicht nutze ich sogar noch sowas wie Kabelbinder, um das Ganze noch besser zu strukturieren. Wenn ich jetzt aber einfach Gerät nach Gerät nach Gerät einstecke und sich da so ein riesen Spaghetti-Kabelsalat bildet, dann weiß ich irgendwann nicht mehr ganz genau, welcher Stecker zu welchem Gerät gehört und wenn ich jetzt irgendwo eine Lampe abstecken möchte, ziehe ich vielleicht aus Versehen den Monitor raus. Wenn du jetzt schon mal das Problem in deinem Projekt hattest, dass am Anfang erstmal alles super läuft, aber irgendwann macht Cloud oder Codex bei der Behebung eines Fehlers z.B. ein anderes Feature kaputt, dann ist das genau dieser Effekt. Und wenn man sich jetzt noch mal die aktuellen Probleme von Coding Agents in Erinnerung ruft, also sowas wie stille Annahmen, Overengineering, Abkürzung, vergessener Kontext, dann sind das alles Dinge, die ein System schwerer verständlich machen.

Sprich, ein Coding Agent kann diesen Kreislauf sogar noch beschleunigen, weil sie viel schneller Code produzieren, als du ihn überhaupt reviewen, geschweige denn verstehen kannst. Das führt natürlich auch zur Frage, wie gut ist denn der Code, den Cloud Code und Codex heute schreiben? gibt's ein paar interessante Analysen, die wir uns mal anschauen wollen. Wo alle Analysen einstimmig waren, ist, dass heutige Modelle syntaktisch korrekten Code ohne weiteres hinbekommen. Also, das heißt, im einfachen Sinne einfach Code ohne Rechtschreibfehler zu schreiben. Veracode z.B. eine Firma für Softwaresicherheit bezeichnet das in ihrem aktuellen Report also als absolut gelöst. Sonar, ein anderes Unternehmen hat sich z.B. mal Opus 5.5 genauer angeschaut und das Modell schreibt z.B. im Vergleich zu seinem Vorgänger Opus 5 ein Viertel weniger Code und hat deutlich weniger Auffälligkeiten.

Trotzdem besteht immer noch ungefähr jede achte Lösung ihre Tests nicht. Anders sieht das beim Thema Sicherheit aus. Endor Labs z.B. hat Opus 5.5 mit Cloud Code an echten Aufgaben in echten Open-Source-Projekten getestet. Funktioniert hat der Code in knapp 70% der Fälle. Sicher war er aber nur in einem Drittel der Fälle. Codex mit GPT-6 Astra lag bei der Sicherheit fast gleich auf. Und laut Veracode hat sich die Sicherheitsquote über alle getesteten Modelle hinweg seit vier Jahren praktisch fast gar nicht bewegt. Dazu kommt eine Auswertung der Software Improvement Group über mehr als 400 Milliarden Zeilen echter Unternehmenssoftware und deren Ergebnis war, dass KI-generierter Code immer noch rund doppelt so viele Sicherheitsverstöße wie menschengeschriebener Code hat und der zudem noch deutlich schlechter wartbar ist. Und je größer die Codebase wird, desto schlechter wird am Ende die Qualität. Fairerweise muss man sagen, Sonar, Endor Labs und Veracode verkaufen allesamt Tools für Codeanalysen und Sicherheit. Dementsprechend sind die Aussagen mit Vorsicht zu genießen, aber die Richtung ist eben bei allen gleich.

Das heißt also beide Lager, die ich eingangs genannt habe, haben Stück weit Recht. Funktionierenden Code liefern Cloud Code und Codex inzwischen natürlich absolut zuverlässig, aber funktionaler Code und sicherer und wartbarer Code sind zwei verschiedene Dinge und hier gibt's eben definitiv noch Luft nach oben. Wenn dir das Video bis hierhin gefällt, dann würde ich mich sehr über ein Like und ein Abo von dir freuen. Aktuell haben ca. 80 % der Zuschauer den Kanal noch nicht abonniert und mit dem einen Klick würdest du mir wirklich weiterhelfen. Also, vielen Dank und weiter geht's. Vielleicht lösen das künftig Modelle, das kann natürlich sein oder auch nicht, aber was ich besonders spannend finde, ist auch, dass Coding Agents eine neue Kategorie von Software aufgemacht haben und zwar Wegwerfsoftware. Sprich, das ist einfach Software, bei der eigentlich soweit nichts passiert, wenn sie ausfällt, kaum jemand hängt davon ab, kein anderes System greift darauf zu und man kann das Ganze in wenigen Minuten oder Stunden eben neu entwickeln, plus Wartung kostet dabei auch nichts. Ein paar Beispiele dazu habe ich in meinem letzten Video geliefert, wo ich mir einfach ein paar persönliche Tools entwickelt habe, um z.B. meine Systemperformance zu überwachen oder meinen Festplattenspeicher zu analysieren und zu managen. Oder ich habe mir auch einen kleinen lokalen Whisper Flow Clone gebaut. Alles also kleine Helfer, die mich im Alltag unterstützen. Und bei so einer Software ist die Codequalität komplett egal, denn die Risiken, die sich über die Zeit aufschaukeln, die gibt's hier eigentlich gar nicht. Man darf das eben nur nicht verwechseln mit produktiver, langlebiger Software, die jahrelang läuft, von vielen Nutzern verwendet wird und wo ein Ausfall im Zweifelsfall richtig teuer werden kann.

Und das ist dann die wichtigste Art von Software überhaupt. Was davon trifft denn jetzt genau auf dein Projekt zu? Das kannst du dir recht einfach mit vier Fragen beantworten. Erstens, was passiert, wenn deine Software ausfällt? Zweitens, wie teuer wird es, das Ganze neu zu entwickeln? Drittens, wer oder was hängt davon ab? Also, Menschen oder auch andere Systeme? Und viertens, wie viel Wartung braucht das Ganze? Ist die Antwort bei allen vier Fragen wenig, dann hast du quasi eine Wegwerfsoftware. Wenn die Antwort bei allen vier Fragen viel ist, dann hast du eine langlebige Software. Dazwischen gibt's natürlich ein ganzes Spektrum. Das heißt jetzt, je weiter rechts dein Projekt hier auf auf Skala liegt, desto mehr Sorgfalt braucht es am Ende bei der Entwicklung und Planung. Und da liegt eben auch das Problem, was ich gerade bei vielen Leuten sehe, denn die entwickeln einen Software-as-a-Service für echte Kunden, gehen aber dabei vor wie bei einer Wegwerfsoftware. Denn sobald du echte Kundendaten verarbeitest oder echte Kunden im Spiel sind, musst du dein Projekt wie ein langlebiges Softwareprojekt behandeln. Bevor ich dir gleich zeige, wie ich das Ganze in der Praxis umsetze, hier noch ein kurzer Einschub und zwar in Zusammenarbeit mit meinem Partner und dem Sponsor dieser Sektion DL Education. Denn wie du mit Coding Agents Software entwickelst, auf die du dich verlassen kannst, das lernst du auf dem Digitale Leute Summit. Der findet am 17. und 18. November in Köln statt, also schon in wenigen Wochen. Das ist eine der führenden Konferenzen in Deutschland im Bereich Product Engineering und UX Design. Ich war die letzten Jahre selbst auch schon vor Ort und bin dieses Jahr sogar als Speaker mit dabei. Am 17. November startet das Ganze mit dem AI Deep Dive Day, das heißt also ein ganzer Tag mit praxisnahen Sessions, wie du KI in Produkt Design und Engineering Teams einsetzt. Da geht es also vor allem darum, wie du selbst direkt in die Umsetzung kommst. Am zweiten Tag, dem Conference Day, kommen dann über 45 internationale Speaker zusammen, unter anderem von OpenAI, Google DeepMind, YouTube und Microsoft. Und du hast die Möglichkeit, dich mit vielen Leuten aus dem Produkt- und KI-Bereich zu vernetzen. Sicher dir also jetzt am besten noch eins der begrenzten Tickets und mit dem eingeblendeten Code sparst du noch mal 15 %. Den Link und den Rabattcode findest du in der Videobeschreibung. Ich würde mich auf jeden Fall freuen, wenn wir uns vor Ort sehen. Ganz egal, wo dein Projekt auf dem eben gezeigten Spektrum liegt, das Entscheidende ist eigentlich die Sorgfalt für dein Projekt einfach in Anführungszeichen billig zu gestalten.

Denn wenn Qualität dich eigentlich nichts kostet, dann ist es auch egal, ob aus einem Wegwerftool später irgendwann plötzlich doch mal ein Produkt werden sollte. Die Hebel, die du dafür hast, sind Standards, Prüfungen, die automatisch laufen, Testings und Leitplanken, die quasi von Anfang an gelten. Und bei mir sieht das z.B. wie folgt aus: Unabhängig vom Stack nutze ich Context Management und einen standardisierten Ablauf für meine Entwicklungsprojekte. Sprich, ich habe eine feste Struktur in meiner Cloud Markdown Datei oder analog der Agents Markdown Datei, also eine Projektbeschreibung, Informationen zum Text Deck, Verhaltensregeln und Infos zur Projektstruktur. Außerdem lasse ich Cloud in einem festgelegten Zyklus entwickeln. Der startet beim Festlegen der Anforderungen in Form von Spezifikationen, geht dann über in die Aufgabenplanung, dann haben wir die Implementierung und zum Schluss gibt's dann noch einmal die Qualitätssicherung und das Deployment. Das heißt, bei jeder Funktion, die ich implementiere, geht dieser Zyklus quasi wieder von vorne los. Bevor Cloud überhaupt irgendeine Zeile Code schreibt, gibt jedes Feature, wie gesagt, eine Spezifikation. Die beschreibt, was das Feature können muss, welche Sonderfälle es gibt und woran ich erkenne, dass das Feature fertig implementiert ist. Dazu habe ich mir einen eigenen Skill gebaut, der dann ein Template für eine Spezifikation nutzt, damit ich am Ende immer wieder die gleiche Art von testbaren Anforderungsdokumenten habe. Innerhalb einer Spezifikation schreibt mir der Agent auch Akzeptanzkriterien runter, die sowohl er selber testen kann, als auch ich später, wenn ich die Funktion für ihn abnehme. Für die Funktion werden entweder vor der Implementierung schon Tests geschrieben nach dem Test-Driven-Development-Prinzip oder eben danach. Die Prüfung soll dann am Ende von einem separaten Agent durchgeführt werden, der nur die Spezifikation und das fertige Ergebnis kennt, aber eben nicht den Weg dahin.

Der prüft dann auch jedes Akzeptanzkriterium durch und versucht aktiv Sicherheitslücken zu finden. Der schreibt mir dann am Ende auch einen kompletten Testbericht, in dem ich mir noch mal selbst ein Bild von der Qualität machen kann. Stichwörter sind hier auch noch Regressionstests, Integrationstests und End-to-End-Tests. Dazu habe ich auch ein eigenes Video gemacht, dass ich dir hier mal verlinke. Schau dir das gerne mal an, wenn dich das Thema interessiert. Zudem läuft dann noch ein sogenannter Linter. Das ist ein Programm, das deinen Code automatisch auf Fehler und Regelverstöße prüft. Genauso wie z.B. eine Typprüfung von TypeScript, die z.B. merkt, wenn man irgendwo eine Zahl erwartet, aber am Ende einen Text übergibt. Und nach jeder Umsetzung läuft dann am Ende eben eine Abschlussprüfung inklusive Linter, Typprüfung, Tests. Und das passiert dann eben auch automatisch, ohne dass ich selbst daran denken muss. Wenn du so einen automatischen Ablauf mit Cloud Code, Codex und Co. aufsetzen möchtest, also von der Spezifikation über Planung, Umsetzung bis hin zur Qualitätssicherung, dann kann ich dir an dieser Stelle noch meinen kostenlosen AI Engineering Blueprint ans Herz legen. Da ist genau beschrieben, wie du dabei vorgehst. Den Link dazu findest du in der Videobeschreibung. Also nochmal zusammengefasst, ist die Codequalität egal, wenn KI den Code schreibt? Bei Wegwerfsoftware, ja, absolut egal. Bei Software, die produktiv über einen langen Zeitraum eingesetzt werden muss und dazu gehört jedes Software-as-a-Service mit echten Kundendaten, dann sollte das auf jeden Fall dein Fokusthema sein. Muss Qualität teuer sein? Nein, absolut nicht. Wenn du Standards hast, wie Spezifikation, Tests, automatische Prüfung und so weiter und so weiter, dann laufen die im Hintergrund immer mit. Du musst sie eben nur einmal aufgesetzt haben. Mich würde aber natürlich auch interessieren, wie du vorgehst. Also, wie entwickelst du gerade deine Software und wie machst du dir ein Bild von der Qualität, die am Ende umgesetzt worden ist? Schreib mir das sehr gerne mal in die Kommentare.

Falls dir das Video gefallen hat, dann würde ich mich sehr über ein Like und ein Abo von dir freuen und dann hoffe ich, dass wir uns beim nächsten Video wiedersehen. Also, bis dahin. Mach's gut.
