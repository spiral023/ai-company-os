---
url: https://www.youtube.com/watch?v=ZNQ5Jdn-CwE
titel: "T3 Code: ENDLICH eine Steuerzentrale für ALLE deine Coding Agents (Open Source!)"
autor: "Alex Sprogis"
datum: 2026-10-07
erfasst: 2026-10-11
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-11
source_notiz: 80_Knowledge/Sources/2026-10-07-alex-sprogis-t3-code-endlich-eine-steuerzentrale-fuer-alle-de.md
video_id: "ZNQ5Jdn-CwE"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "407"
---

# T3 Code: ENDLICH eine Steuerzentrale für ALLE deine Coding Agents (Open Source!)

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=ZNQ5Jdn-CwE](https://www.youtube.com/watch?v=ZNQ5Jdn-CwE)

## Videobeschreibung

📌 Links:
Mein kostenloser AI Engineering BLUEPRINT: https://link.alexsprogis.de/Rr6va5

Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/OCiCEq

Webseite: https://t3.codes/
GitHub & Dokumentation: https://github.com/pingdotgg/t3code

---
Mit T3 Code hast du endlich eine Steuerzentrale für alle deine Coding Agents. Egal ob Claude Code, Codex, Cursor, Grok Build oder Github Copilot. Ich habe die App seit mehreren Tagen im Einsatz und bin seit dem nicht mehr zurück zu VS Code. Auch die Desktop Apps von Claude & Codex brauche ich nicht mehr. 

Das Tool ist komplett kostenlos, Open Source und du kannst es mit all deinen vorhandenen Abos nutzen. 

---

Kapitel:

00:00 -  Intro
00:47 - Probleme mit VS Code & Desktop Apps 
02:08 - T3 Code
03:53 - Demo
10:33 - AI Engineering Blueprint

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

Bisher habe ich Software mit Cloud Code und Codex fast ausschließlich in VS Code, also einem Open Source Editor von Microsoft entwickelt. Das heißt also weder in der Cloud Desktop App noch in der Codex Desktop App, denn die Desktop Apps lassen etwas vermissen, was ich in VS Code sehr schätzen gelernt habe und das sind neben ein paar kleineren Funktionen und Shortcuts eben vor allem die Übersichtlichkeit über große Projekte. Allerdings muss man auch sagen, haben die Desktop Apps von Cloud und Codex auf der anderen Seite eben wiederum Funktionen, die WS Code heute so nicht abbilden kann. gerade wenn man mit mehreren Agents gleichzeitig an einer App arbeiten möchte. Ich bin jetzt auf ein neues Tool gestoßen, das sozusagen der Harness für Coding Harnesses ist und die Vorteile von es Code als auch den Desktop Apps vereint.

Es ist komplett open source und du kannst es gefahrenlos mit deinen Abos von Cloud und Codex nutzen. Seitdem ich das erste Mal vor über 18 Jahren meine erste Zeile C++ geschrieben habe, war das in VS Code. Auch Jahre danach war das mein tägliches Werkzeug und auch heute mit all den AI Coding Agents habe ich die Flexibilität des Tools erneut lieben gelernt. Die Desktop Apps von Cloud und Codex werden immer besser und haben auch diverse Vorteile. Der integrierte Browser z.B. Ja, mit Annotierungsfunktion, Kommentarfunktion, das macht es eben extrem schnell möglich, bestimmte Bereiche zu markieren und nachzubessern, aber sie lassen eben auch einiges vermissen und es fühlt sich manchmal dann doch sehr umständlich an.

WS Code auf der anderen Seite ist natürlich auch weit weg von Perfekter. Das fängt an beim integrierten Browser. Der zeigt dir zwar deine App an, aber du hast keine Möglichkeit schnell mal eben ein Element zu markieren und deinem Coding Agent dann Änderung an diesem anzuweisen. Es sei denn, du nutzt GitHub Code Pilot, denn diese Funktion wird eben nur für diesen Coding Agent unterstützt. Was mich aber eben vor allem stört, ist, wenn du mit unterschiedlichen Agents und Modellen an einem Projekt arbeiten willst. Nehmen wir Cloud und Codex. Es gibt zwar Erweiterungen für beide, allerdings funktionieren die nur komplett losgelöst voneinander. Du kannst also nicht mal eben mitten in der Konversation von einem auf den anderen Agent wechseln, sondern muss das umständlich über manuelle Handovers regeln. Außerdem gibt es zwar eine Übersicht über parallelufende Agents, unterstützt wird das allerdings auch nur wieder bei Gitub Copilot. Also habe ich mich ein bisschen auf die Suche gemacht und ich habe mir viele Lösungen angeschaut von Hörder, Warp, Conductor und Co. Aber ich muss sagen, ich bin auch nach wie vor kein Fan vom Terminal. Ich stehe halt einfach persönlich eher auf schöne Benutzeroberflächen. Dann bin ich auf T3 Code von Theo Brown gestoßen, einem anderen YouTuber und Softwareentwickler und ich habe das die letzten Tage mal ausführlich getestet und muss sagen, ich bin echt begeistert. Aber zuerst mal, was ist überhaupt T3 Code? Es ist laut offizieller Beschreibung ein Agent Hannes Control Service, also letztendlich ein Hannes für Coding Hannes oder einfach gesagt eine Steuerzentrale für all deine Coding Agents. T3 Code ist kein eigenes Modell und auch kein eigener Agent. Es steuert aber die Agents, die du schon installiert hast und integriert dafür eben auch alle bestehenden Abos. Das heißt Cloud Code, Codex, Cursor, Grock, Antti Gravity, Open Code, Copilot und viele mehr. Jetzt fragst du dich, vielleicht geht das überhaupt gefahren los? Dennopic hat ja in ihren eigenen Nutzungsbestimmung verboten, das eigene Abo mit Third Party Services zu nutzen.

Da kann ich dir sagen, ja, das geht, denn T3 Code nutzt die Cloud Code CLI und damit eben den offiziellen Weg zur Nutzung von Cloud Code aus anderen System heraus. T3 Code ist also als Desktop App, als Webapp und Mobile App verfügbar und ist wie gesagt komplett open source und damit eben auch kostenlos. Wenn dir die Anwendung also grundsätzlich gefällt, du vielleicht noch ein z D Features on top hättest, dann du dir einfach das Repository und entwickelst dir deine eigene Version von T3 Code. Wenn dir das Video bis hierhin gefällt, dann würde ich mich sehr über ein Like für das Video und ein Abo für den Kanal freuen. Aktuell haben nämlich ca. 80% der Zuschauer den Kanal noch nicht abonniert und mit dem einen Klick würdest du mir wirklich sehr weiterhelfen. Also vielen Dank und weiter geht's. Die App findest du einfach unter t.codes. Codes habe ich dir natürlich direkt in der Videobeschreibung verlinkt und dann landest du hier auf der Landing Page.

Hier kannst du direkt die App für Macos runterladen oder auch direkt zum Gitter Repository springen, um dir das Ganze dann zu forken und gegebenenfalls auch für dich anzupassen. So, hier sieht man schon so ein bisschen, das orientiert sich natürlich an den bestehenden Desktop Apps, aber kombiniert dazu eben noch super sinnvolle Funktion. Das heißt, wir haben hier links alle unsere Agents und unsere Sessions, unsere Threads in der Mitte dann eben die Konversation und rechts können wir uns alles mögliche einblinden lassen von den DFs über Browser, über die Filc. Schauen wir uns aber auch gleich in der Praxis an. Was wie gesagt extrem spannend ist, ist, dass du einfach deine eigenen Subscriptions mitbringen kannst. Das heißt, egal was du gerade nutzt, du kannst es in T3 Code einfach weiterhin nutzen. Plus, du hast super viele Abkürzung, um mal schnell ein Pull Request zu machen, um die Pull Requests dir anzuschauen, zu merchen etc. Also, ich würde sagen, lass uns direkt mal reinspringen. So, ich bin jetzt hier direkt in der App und es sieht zum Start natürlich erstmal aus wie jede andere Desktop App. Ja, ich habe hier links alle meine Sessions und ich habe hier in der Mitte mein Chatfenster, wo ich jetzt direkt eine neue Session starten kann.

Wenn ich eine neue Session starte, ja, dann kann ich jetzt hier einfach neuen Thread ausführen sozusagen und dann meine bestehenden Projekte auswählen, für die ich jeweils einen neuen Thread starten möchte. Ich kann aber natürlich auch ein gänzlich neues Projekt starten, kann hier ein Ordner, den lokalen auswählen oder auch ein Gitter Repository, was hier existiert. Ich habe auch Zugriff zu Gitlab, zu Elser Devops etc. Das muss natürlich einmal initial konfiguriert werden. Ja, und dann kann ich hier mein Prompt eingeben. Ich kann natürlich direkt aus allen Modellen wählen, die ich hier verbunden habe.

Wenn du die App erstmalig installierst, dann werden deine Abos automatisch erkannt und dann hier eben schon zum Tool hinzugefügt. Also das ist super nahlos, super angenehm und im Anschluss kannst du die dann eben einfach hier jeweils auswählen. Also ich habe ja wirklich alle Modelle zur Verfügung. Worauf du achten solltest, ist, dass er hier standardmäßig mit Full Access arbeitet. Du kannst das natürlich auch in den Settings umstellen und z.B. in den Automodus switchen. Ja, so können wir immer noch destruktive Befehle vermeiden oder das automatische ausführen vom destruktiven Befehl. So, hier links sehe ich alle meine Sessions.

Da können wir jetzt gerade sehen, hat hier ein Agent gerade fertig gearbeitet, ist jetzt hier auf dann und wenn wir hier mal reinklicken, ich habe hier gerade z.B. ein bisschen was für eine Retargeting Kampagne ausgearbeitet, dann habe ich mir das Setup hier so ausgestellt, dass ich hier links meinen Chatboard habe, in der Mitte dann eben meine Dateien und rechts meine Ordnerstruktur aus meinem Business OS. So, ich kann h natürlich dann direkt in die Markt Dateien reingehen, kann h Änderung machen, kann mir das aber auch natürlich jederzeit hier in der Vorschau anzeigen lassen. Das ist natürlich super cool. So und da sind wir dann schon sehr nah an VS Code von der Anordnung von der Ansicht her. Ich kann natürlich auch hier jederzeit weitere Dateien öffnen.

Das Ganze wird dann hier in Tabs dargestellt. Kann super einfach hin und her springen. Sehr, sehr cool gemacht. Wenn wir jetzt mal hier in ein Projekt reinspringen, ich habe jetzt z.B. hier gerade mein Software, also Serviceel am laufen. Ja, dann kannst du hier sehen, gibt es auch die Browser Vorschau, die ich mir hier dazu holen kann und hier gibt es eben auch diese beliebten Features aus der Codex App z.B. oder auch aus der Cloud App. Ich kann hier einfach ja Sachen markieren, eben das hier direkt mitgeben und dann wird das eben an die Kommensation angehängt und ich kann direkt damit eben weiterarbeiten.

So, wenn ich jetzt mehrere Agents parallel am laufen habe, zeigen wir mal, ich starte jetzt mal eine neue Aufgabe. So, dann wandert der hier unten in den Bereich working. Da finde ich also immer meine aktuellen Agents, die am laufen sind. Da drunter gibt's dann noch die Settled Sektion. Da es dann alles, was sozusagen schon länger nicht mehr genutzt worden ist oder von mir archiviert worden ist, was ich dann nicht mehr in meiner Hauptansicht sehen möchte. Ja, aber so bekomme ich hier unter Working eben immer eine Übersicht über alle Agents, die hier im Hintergrund arbeiten und kann mich dann eben ja währenddessen um andere kümmern.

So, wenn er jetzt fertig ist, dann springt er eben wieder nach oben und ich kann damit weitermachen. Ansonsten sehe ich hier auch direkt meine aktuellen Limits und Ausgaben. Kann ja direkt auch switchen zu meinen Limits. So sieht's bei mir hier aktuell gerade aus. Ansonsten kann ich aber auch alle Pull Requests sehen, die von mir offen sind oder jetzt auch für das Projekt offen sind. Kann da direkt reinschauen und dann tatsächlich auch das Ganze direkt merchen, wenn ich möchte. Ansonsten haben wir hier in den Settings noch die unterschiedlichsten Möglichkeiten. Also hier kann ich z.B. den Permissionmodus standardmäßig festlegen. Wenn ich jetzt z.B. auf Automode umstellen möchte. kann auch festlegen, ob er hier für jeden neuen Thread, den ich starte, auch ein neuen Worktree anlegt. Finde hier wie gesagt also alles mögliche an Einstellung, die ich konfigurieren kann.

Ich laufe hier aktuell auf der Nightly Version. Es gibt hier die Stable und die Nightly Variante. Und bei der Nightly Variante habe ich sozusagen schon alle aktuellen Updates mit drinne. Das sind natürlich dann gerade frisch deployte Geschichten, die womöglich noch Bugs enthalten. Also da muss man sich natürlich dem bewusst sein. Allerdings ist vor allem hier dann die Möglichkeit eben mitten in der Session sozusagen einfach das Modell zu switchen und hier dann in dem Fall mit GPT 6.1 ein weiterzuarbeiten und das ist natürlich eine extrem coole Möglichkeit schnell Sachen reviewen zu lassen von anderen Modellen, um da wieder andere Perspektiven reinzubringen. Genau.

Ansonsten kann ich hier natürlich die Appearance verändern. Kann hier also, wenn ich möchte, das Aussehen entsprechend anpassen. Kann hier den Kontrast konfigurieren, mir die di Colors umstellen, wie ich möchte etc. Hier haben wir dann auch noch mal die ganzen Shortcuts, die natürlich auch super cool sind, um schnell hier in diesem Tool zu navigieren. Ich habe hier die ganzen Provider, die ich konfigurieren kann. Also neben den Standard Providern kann ich natürlich hier alles mögliche weitere direkt hinzufügen. Und was natürlich auch ganz cool ist, unter den Connections kann ich natürlich auch externe Umgebung einrichten. Ja, wie hier z.B. einen Hostinger VPS, mit dem ich dann eben losgelöst von meinem Rechner entwickeln kann. Das kann natürlich auch super sinnvoll sein, wenn du jetzt hier nicht primär auf deinem eigenen Rechner entwickelst, sondern vielleicht auf einem Zweitrechner oder eben auch auf einem virtuellen Server, dann kannst du das natürlich ganz einfach machen. Wie gesagt, es gibt auch eine Mobilapp, das heißt auch darüber kannst du sozusagen jederzeit auf deine Entwicklungsumgebung zugreifen und das von da aus steuern.

Wenn ich hier noch mal in so ein Verlauf reingucke, dann habe ich hier oben rechts auch immer so ein paar Shortcuts, die ich direkt ausführen kann. Also ich kann jetzt z.B. direkt die Branches wechseln, was ziemlich cool ist. Ich kann direkt Commit und Push ausführen mit einem Klick. Ich kann aber auch weitere Skripte hier einfach hinzufügen. Also, wenn ich jetzt sage, ich möchte jetzt z.B. den Def Server starten, ja, dann nenne ich den Befehl mal npm Run Def und lass das einfach als Befehl ausführen. Speicher mir das als Aktion und dann habe ich den hier oben direkt mit angeheftet und kann ih einfach ausführen und dann wird hier automatisch eben der Befehl ausgeführt. Ja, und ich kann jetzt hier dann mir einfach meine Website anschauen, indem ich die dann hier z.B. Spiel einmal aufrufe. Genau.

Wenn du jetzt mehrere Agents in T3 Code zusammenbringst, stellt sich als nächstes die Frage, wie sorgst du überhaupt dafür, dass die auch zuverlässig an deinem Projekt arbeiten? Und genau dafür habe ich meinen kostenlosen AI Engineering Blueprint erstellt. Wahrscheinlich hast du das auch schon erlebt, wenn du Apps mit AI entwickelst, dann sind die ersten 80% meistens super schnell gemacht und dann wird's aber Schritt für Schritt immer schwieriger, denn mit jedem weiteren Feature vergisst der Agent mehr und mehr, was du mit ihm mal festgelegt hast. Ja, das merkst du dann, indem man immer wieder denselben Bug oder immer wieder teilweise auch bestehende Funktionen kaputt macht und irgendwann verlierst du selber als auch dein Coding Agent den kompletten Überblick über das Projekt. Ein Grund für dieses Problem ist, dass das Wissen über dein Projekt komplett im Chatverlauf liegt. Der Blueprint zeigt dir deswegen, wie du dieses Wissen festhältst und daraus einen festen prüfbaren Ablauf für deine Coding Agents entwickelst. Dafür gibt es im Blueprint verschiedene Bausteine vom Projektgedächtnis über Spezifikation, Architektur, Plan, Umsetzung, unabhängige Prüfung, Lightplanken und so weiter und so weiter. Das Ganze funktioniert to unabhängig, egal ob du also Cloud Code, Codex, Copilot, Open Code nutzt. Das Ziel ist einfach, dass deine Agents nachvollziehbar arbeiten und du auch nach dem 20. Feature noch den Überblick hast und guten Gewissens sagen kannst, dass deine Software genau das leistet, was du eben auch geplant hast. Den Link zum Blueprint findest du in der Videobeschreibung. Da kannst du dir den einfach kostenlos runterladen.

Also, es lohnt sich auf jeden Fall mal einen Blick auf T3 Code zu werfen, gerade wenn du mehrere Coding Agents hast und immer noch nach einem Weg suchst, die alle irgendwie sinnvoll unter einen Hut zu bringen und mit denen auch gleichzeitig arbeiten zu können. Das Ganze ist noch eine Alpha Version. Das heißt, also natürlich kann es vorkommen, dass Bugs existieren. Dessen sollte man sich auf jeden Fall also bewusst sein. Wenn du aber selbst die Entwicklung mitgestalten möchtest oder vielleicht auch mit deinem eigenen Fork einen eigenen Coding Agent Hannes für Coding Agents bauen möchtest, dann ist das hier eine super Möglichkeit. Hast du T3 Code schon mal ausprobiert oder welches Tool nutzt du gerade zur Entwicklung mit Cloud Code und Codex?

Schreib mir das gerne mal in die Kommentare. Falls dir das Video gefallen hat, dann lass gerne ein Like und ein Abo für den Kanal da. Ansonsten hoffe ich, dass wir uns dann beim nächsten Video wiedersehen und bis dahin mach's gut. Yeah.
