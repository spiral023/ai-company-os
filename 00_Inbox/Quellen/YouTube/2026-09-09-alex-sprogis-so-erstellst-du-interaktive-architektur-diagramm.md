---
url: https://www.youtube.com/watch?v=YE40EDb1kRk
titel: "So erstellst du interaktive Architektur-Diagramme mit Claude (2026)"
autor: "Alex Sprogis"
datum: 2026-09-09
erfasst: 2026-09-14
typ: youtube
quelle: youtube
status: neu
video_id: "YE40EDb1kRk"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "435"
---

# So erstellst du interaktive Architektur-Diagramme mit Claude (2026)

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=YE40EDb1kRk](https://www.youtube.com/watch?v=YE40EDb1kRk)

## Videobeschreibung

📌 Links:
Cookiebot (10% Sparen über meinen Link): https://usercentrics.sjv.io/alexsprogis10

Mein AI Coding Starter Kit: https://link.alexsprogis.de/QcIwqL

Mein AI Engineering Accelerator (Entwickle ein produktives, sicheres SaaS ohne Vorkenntnisse): https://link.alexsprogis.de/TorUGX

Archify auf Github: https://link.alexsprogis.de/2nisa0
Archify Website: https://link.alexsprogis.de/h5PPQV

-----

Du dokumentierst die Architektur deiner Apps wahrscheinlich noch mit Miro, Figma oder einem anderen Whiteboard-Tool . Das heißt bei jeder Code-Änderung ziehst du alles immer wieder von Hand nach. In diesem Video zeige ich dir Archify - einen Skill für Claude Code, Cursor, Codex und Co., der dir aus einer einfachen Beschreibung oder direkt aus deiner Codebase, interaktive Architektur-Diagramme baut. Ich zeige dir, was Archify kann, wie du es installierst und wie ich damit für ein echtes SaaS-Produkt verschiedene Diagramme direkt aus der Codebase generiert habe.

-----

Timestamps:

00:00 Intro
00:45 Was ist Archify?
01:27 Cookiebot
03:02 Installation
05:14 Diagramme erstellen
08:06 Architekturdiagramm
10:25 Datenflussdiagramm
10:49 Prozessdiagramm
11:25 Workflow-Diagramm
13:10 AI Coding Starter Kit

-----

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

Wenn du die Architektur deiner Apps dokumentieren möchtest, dann nutzt du wahrscheinlich gerade Tools wie Miro, Figma oder irgendein anderes Whiteboard bzw. Diagrammt Tool, auf dem du manuell Boxen und Pfeile hin und her schiebst. Wenn sich dann irgendwas an deinem Code oder an deiner Architektur ändert, dann musst du das Diagramm immer wieder aufwendig nachziehen. Ich will dir heute eine Alternative zeigen und zwar einen Skill namens Archify, der im AI Coding Bereich gerade komplett durch die Decke geht. Den kannst du ganz einfach für Cloud Code, Cursor, Codex und Co. installieren und der gestaltet dann aus deiner Beschreibung oder eben auch direkt aus deiner Codebase interaktive Architekturdiagramme. In diesem Video zeige ich dir also was Archify kann, wie du es installierst, wie du Diagramme aufsetzt und welche Arten von Diagramme du für deine Apps und Prozesse gestalten kannst. Archify ist ein kostenloses Open Source Projekt, das in der AI Engineering Bubble gerade ziemlich die Runde macht. Du beschreibst im Skill einfach, was er genau für dich als Diagramm gestalten soll und er setzt das dann eben direkt um. Das coole ist vor allem, dass er das direkt basierend auf deiner aktuellen Codebase machen kann.

Du kannst also sowas wie Architekturdiagramme, Workflowdiagramme, Sequenzdiagramme, Datenflussdiagramme oder Life Cycle Diagramme erstellen. Das Ganze beschränkt sich nicht nur auf technische Abläufe, sondern du kannst damit auch Businessprozesse visualisieren. Von Archify bekommst du dann nicht einfach nur ein Bild zurück, sondern ein wirklich interaktives Diagramm, das dir Details zu einzelnen Knoten und Verbindung anzeigt. So und wie das im Detail aussieht, da wollen wir jetzt mal reinschauen. Vorher will ich dich aber noch auf ein wichtiges Thema aufmerksam machen, wenn du deine eigene App oder live bringen willst, die du mit AI entwickelt hast. Und hier kommt mein Partner und heutiger Sponsor dieser Sektion ins Spiel und zwar ist das User Centrix. Wenn du dir mit Cloud Code oder einem anderen Agenten selbst eine Website oder App entwickelst und dann eben externe Dienste einbindest, wie Analytics Tools, Session Recordings oder Error Tracking, dann benötigst du unbedingt einen Constantban Banner, über den die Benutzer ihr Einverständnis zum Speichern dieser Daten geben. Das ist so gesetzlich vorgeschrieben, denn ohne darfst du diese eben nicht verarbeiten.

Glücklicherweise gibt es dafür CookieBard von User Centrix, eine Content Management Plattform, die du als Nippit ganz einfach in deine Website oder deine App einbauen kannst. Cookie Bot trackt und klassifiziert deine Cookies automatisch, blockt sie bis jemand zugestimmt hat und aktualisiert sich automatisch, wenn sich Regulierungen z.B. auch ändern. Abgedeckt werden unter anderem die DSGVO, E-Privacy und CCPA bzw. CPRA. Die Einrichtung ist super einfach gemacht. Du kannst einfach den Link in der Videobeschreibung nutzen, dir einen Trial Account erstellen und dir direkt einen Cookie Content Banner anlegen. Das Code snippet, was du dann bekommst, lässt du einfach von deinem Coding Agent wie Cloud Code in deiner App oder hinterlegen. Im Anschluss kannst du dann einfach einen Scan durchlaufen lassen, damit dein Constantban Banner konfiguriert wird. Du hast auch die visuelle Gestaltung komplett selbst in der Hand und kannst das Design nach deiner eigenen Vorstellung anpassen. Für kleine Webseiten ist Cookie Bot komplett kostenlos. Für größere Projekte starten die bezahlten Pläne bei 7 € im Monat.

Wenn du das also selber mal ausprobieren möchtest, dann klick einfach mal auf den Link in der Videobeschreibung. Da habe ich dir eine 14 Tage Testversion mit allen Premium Features verlinkt. So und jetzt zurück zu Archify. Starten wir mit einem kleinen Blick hier auf die Webseite. Ich habe dir das natürlich alles verlinkt. Also, ich glaube, hier gibt's primär zwei interessante Unterseiten, die man sich mal anschauen kann. Und zwar hier einmal eine kleine Hilfe, um die richtige Art von Diagramm zu finden, die man für sich selber generieren möchte. Ja, da kann man hier einfach sein US Case eingeben und sich dann eben eine entsprechende Empfehlung ausgeben lassen. Hier gibt es also verschiedene Diagrammtypen, wenn man sich das hier mal anguckt. Ansonsten gibt es hier auch eine schöne Übersicht mit den verschiedenen Typen und den verschiedenen Visualisierungsmöglichkeiten.

Aber ich würde sagen, die deutlich spannendere Seite ist das Gitterpo, denn hier wollen wir uns natürlich einmal direkt den Installationsbefehl herholen. Also kopieren wir das Ganze und dann geht's in unsere Entwicklungsumgebung. Wenn du hier also in der Cloud Desktop App unterwegs bist, dann gibt Cloud entweder also einfach den Link vom Repository und lass ihn den Skill automatisch installieren oder öffne hier einmal den Terminal und für den Befehl aus. Ich persönlich bevorzuge Arbeit in einer IDE, also einem Code Editor wie z.B. VS Code, weil ich hier die Übersicht einfach deutlich besser finde, gerade bei größeren Softwarep Projekten.

Ja, da habe ich hier meine Ordnerstruktur, ich habe hier den Inhalt meiner Dateien und ich habe hier rechts die Cloud Extension. Das kann man zwar auch so ein bisschen über die Cloud Desktop App konfigurieren, ist aber lange nicht so komfortabel wie hier. Okay, so installieren wir das Ganze also einmal. Ich starte hier mal einen neuen Terminal und dann gebe ich hier einmal den Befehl ein. So, dann ziehe ich das hier mal ein bisschen größer und dann sehen wir direkt wird das Ganze installiert und uns werden hier direkt die Coding Agents vorgeschlagen, für die das Ganze dann installiert werden soll. Cloud Code ist ja auch schon vorausgewählt, also kann ich hier direkt bestätigen. Simlink kann ich einfach auch auswählen. Ist einfach komfortabel, wenn wir hier mit mehreren Coding Agents an einem Projekt arbeiten.

So, also füllen wir die Installation einmal aus und dann geht's weiter. So, das Ganze ist jetzt schon installiert. Das heißt, ich kann jetzt das Ganze hier einfach schließen und anfangen mir Diagramme für meine Codebase zu erstellen. Wenn dir das Video bis hierhin gefällt, dann würde ich mich sehr über ein Abo von dir freuen. Aktuell haben nämlich ca. 75% der Zuschauer den Kanal noch nicht abonniert und mit dem Einklick würdest du mir wirklich sehr weiterhelfen. Also vielen Dank und weiter geht's. Ich bin jetzt ja hier in einem fertigen Software, also Service Projekt, was tatsächlich auch schon live ist und ich kann jetzt hier natürlich die verschiedendiagramme erstellen lassen. Also würde ich einfach mal sagen, wir fragen einfach mal Cloud, welche Art von Diagrammen er hier vorschlägt, die wir mit Archify aufsetzen können. Also, ich tippe jetzt hier mal den Befehl Archify und dann gebe ich ihm hier mal mit.

Bitte erstell mir ein paar Vorschläge von Diagramm, die du mir passend zu dieser Applikation, zu diesem Projekt hier erstellen kannst. Er kommt jetzt direkt mit einer Auswahl von vier verschiedenen Diagrammen, die ihr mir hier vorschlägt. Und als allererstes mal natürlich eine Gesamtübersicht der Architektur. Ja, das ist auch der klassische Fall, den wir mit Archify abdecken können. Also einmal zu gucken, okay, aus welchem System besteht denn eigentlich unsere Anwendung? Wo gibt es Abhängigkeiten, wie sind die Verbindungen miteinander, welche Daten werden ausgetauscht? Genau das wollen wir uns gleich mal anzeigen lassen. Vielleicht einmal zum Hintergrund. Es geht hier um eine SAS Applikation, die Feedback für Produkte einsammelt und die eben auswertet und dann eben Handlungsempfehlung gibt. Das kann sowas sein wie Daten aus Umfragen, das können Bewertungen sein, z.B. aus dem App Store oder ähnliches und die werden in dieser App dann aufgearbeitet durch eine KI Integration und dann in einen ausführbaren Report umgesetzt. So und demnach zeigt er mir hier eben auch noch an, z.B. hier eine Workflow Feedback Analyse. Das heißt also einmal den kompletten Durchlauf der Kernfunktion der Applikation oder vielleicht auch nur den Zahlungsprozess.

Ja, hier ist Stripe mit angebunden, das kann auch eben sinnvoll sein oder eben auch nur verschiedene Datenflüsse hier. Ich starte jetzt einfach mal mit der Architekturübersicht und damit machen wir mal weiter. Das Diagramm hat er jetzt hier angelegt und zwar mal mit dem Typ Architecture. Gibt mir hier noch mal die kompletten Details und wir können jetzt eben direkt mal reinschauen. Und zwar gibt es jetzt hier unter Docs, unter Diagrams eben einen neuen Ort, wo diese Diagramme gespeichert werden. So und ich habe mir jetzt nicht nur eins generiert, ich habe noch ein paar weitere generiert. Dementsprechend ist der Ordner hier relativ voll. Und was wir hier finden, was die Diagramme betrifft, sind einmal die HTML Dateien dazu. Also hier haben wir jetzt z.B. unser Architekturdiagramm. Das heißt, dazu gibt es immer ein HTML File, was dann gleich die Visualisierung ist und das Personal Jason File dazu, aus der dann die Visualisierung erstellt wird. Und wir haben hier verschiedene Bilddateien.

Das heißt also Cloud prüft bei der Entwicklung dieses Diagramms immer wieder auch selbst, ob das Ergebnis schon fertig ist. macht sich also Screenshots von der HTML Visualisierung, prüft dann wieder, arbeitet nach und macht das eben so lange, bis die HTML-dei dann eben vollständig visualisiert und funktional ist. So und deswegen entstehen hier eben auch Bilddateien. Okay, lass uns mal in so ein Architekturdiagramm mal reinschauen. Ich öffne das hier mal im integrierten Browser und mach Cloud hier mal zu. So, und hier haben wir jetzt unsere Software a Service Applikation. erstmal vielleicht generell, also genau hier ist jetzt das Diagramm, wir haben hier ein paar Einstellungsmöglichkeiten.

Wir können hier in den Light Mode wechseln, falls uns das lieber ist. Es gibt hier auch verschiedene andere Layouts, z.B. hier das Signalflow Design oder vielleicht eher eine Blueprint Ansicht oder der Editorial Stil. Ich bleibe jetzt allerdings mal beim klassischen Stil. Ja, dann haben wir hier so ein Presentmus, dann werden alle anderen Details ausgeblendet und wir können uns das Ganze sogar auch exportieren. Also z.B. als PNG, als JPEG, als SVG etc. So, aber lass uns mal hier in das Diagramm reinschauen. Ich mache das mal ein bisschen größer. Und zwar, was haben wir hier? Wir haben hier einmal unseren Nutzer, der arbeitet mit unserer Note JS App, also einer NextJ App. Das sehen wir auch hier. Hier haben wir also den App Container, der dann wiederum mehrere Komponenten enthält.

Hier sehen wir auch ganz gut die Datenflüsse, was hier jeweils übertragen wird. Dann haben wir unser Backend, das heißt hier haben wir Superbase Cloud angebunden. Das ganze ist in Frankfurt gehostet. Wir haben hier die Authentifizierung. Wir haben hier die eigentliche Datenbank dahinter. Können das auch jeweils anklicken. Also haben dann auch wiederum verschiedene Details zu den jeweiligen Komponenten bzw. Knotenpunkten hier. Und dann gehen hier von den Server Actions aus die Verbindung zu den externen Systemen. Das heißt, wir haben hier Upsash unser Rate Limiting, wir haben Declauded API, wir haben Stripe als Zahlungssystem, wir haben Brevo für transaktionale E-Mails und hier noch Better Stack für das Error Tracking. Und auch hier sehen wir alle Details. Das Ganze ist hier vorkategorisiert. Wir haben hier die Quelle, also die Dateien, in denen die Anbindung konfiguriert ist und wir haben die Infos zu eingehenden und ausgehenden Datenström. Genau, da drunter gibt's noch ein paar andere Informationen, aber grundsätzlich ist es das hier schon. Es gibt jetzt hier noch verschiedene Modi, die man konfigurieren kann oder die man sich anschauen kann. Z.B. den Pathmus.

Da klicken wir z.B. zwei Knotenpunkte an und können uns dann eben Details dazu anzeigen lassen. Wir können uns hier noch eine Map anzeigen lassen, um noch mal ein bisschen Übersichtlichkeit zu bekommen. Ja, und können auch hier noch mal verschiedene Knotenpunkte miteinander vergleichen und uns die Beziehung zueinander anschauen. Ich habe jetzt hier noch mal einen anderen Diagrammtyp mir erstellen lassen und zwar geht es hier um eine konkrete Funktion und zwar das Einfügen von Feedback und dann eben über die Analyse bis zum fertigen Report. Das heißt, also wir haben hier so verschiedene Stages und sehen ganz genau, welche Aktionen hier pro Stage durchgeführt werden und auch wieder, wie die verschiedenen Knotenpunkte miteinander in Beziehung stehen und welche Datenpunkte ausgetauscht werden. Hier noch ein weiterer und zwar jetzt hier kein technisches Diagramm, sondern den Geschäftsprozess der App, der hier visualisiert wird. Und zwar genau startet das Ganze mit der Registrierung, dann muss ein Pro Abo abgeschlossen werden. Dann muss ich einmal 100 Credits zahlen, um hier eine Feedbackanalyse erstellen zu können. Dann kippe ich das Feedback rein, lass die KI analysieren, bekomme am Ende hier den Report, kann dann eben Prioritäten ableiten bzw. Also, es werden mir Maßnahmen angezeigt und ich kann dann entscheiden, okay, mache ich weiter oder kündige ich am Ende mein Abo, wenn die App sozusagen ihren Zweck erfüllt hat und ich sie nicht länger brauche. Neben den technischen Workflows oder auch den Geschäftsprozessen habe ich jetzt hier auch noch mal mein Arbeitsworkflow dokumentiert, den ich mit meinem Framework, mit meinem eigenen Entwicklungsframework hier vornehme. Und zwar das Ganze startet natürlich mit einer Produktidee, sei es für ein neues Produkt oder für ein bestehendes Produkt. Dann initialisiere ich einmal das Projekt. Wenn es bereits ein bestehendes Projekt gibt, dann würde sozusagen einmal eine Analyse und eine rückwirkende Dokumentation für dieses bestehendees Softwaresystem stattfinden.

Ansonsten bei Greenfield Projekten ist es aber so genau Projekt wird initialisiert, alle relevanten Dokumente wie PAD etc. werden angelegt. Die Anforderungen der Anwendung werden runtergebrochen in einzelne Features und dann kann ich für jedes Feature anfangen eine Spezifikation zu schreiben. Dann wird das Systemdesign vorgenommen über den Architecture Skill. Das heißt, da wird dann eben geschaut, okay, welche Seiten müssen erstellt werden, welche Komponenten pro Seite und wie steht alles miteinander in Verbindung. Dann wird das Ganze über Tasks dann in einer Aufgabenplanung übersetzt. Das heißt also Cloud Code oder auch andere Coding Agents bekommen ganz klare Vorgehensweisen, wie sie jetzt den Plan umsetzen. Gehen dann rüber in eine Bildphase, starten also den Implementierungsprozess und dann übernimmt ein unabhängiger QA die Qualitätssicherung, schaut also ist das, was umgesetzt worden ist auch tatsächlich das was geplant worden war, wurde ausschließlich das entwickelt, was am Anfang in der Spezifikation festgelegt worden ist. schreibt dann also Tests, überprüft das und geht am Ende sicher, dass hier alles funktional und fertig für einen produktiven Betrieb ist. Falls das alles erfüllt ist, dann geht's eben ins Deployment und das Ganze wird dann veröffentlicht. Ja, und ich würde sagen, das war einmal ein kleiner Abriss zu Archify. Super hilfreiches Tool und natürlich, wie gesagt, kostenlos. Also probier es gerne mal aus. Wenn du mit Cloud Code an produktiven Softwareprojekten arbeiten willst, dann kann ich dir an dieser Stelle mein kostenloses AI Coding Starter Kit ans Herz legen. Das ist quasi ein Framework und ein Template für agentische Softwareentwicklung und simuliert mit verschiedenen Skills ein echtes Development Team. Dazu gibt es eine komplette Bedienungsanleitung, die dich Schritt für Schritt durchführt, sodass du auch als Einsteiger komplett abgeholt bist. Den Link dazu findest du in der Videobeschreibung. Ansonsten würd mich natürlich jetzt auch interessieren, wie du aktuell deine Architekturdiagramme für Softwarepjekte erstellst. Welche Tools nutzt du dafür und hast du schon mal von Artif gehört und das schon mal ausprobiert? Schreib mir das gerne mal in die Kommentare. Ich hoffe, das Video hat dir gefallen. Falls ja, lass gerne ein Like und ein Abo für den Kanal da. Darüber würde ich mich sehr freuen. Und dann hoffe ich, dass wir uns beim nächsten Video wiedersehen.

Also bis dahin. Mach's gut. Yeah.
