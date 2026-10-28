---
url: https://www.youtube.com/watch?v=r8FYE2ZOj0E
titel: "The secret to building robust frontend apps with agents"
autor: "Matt Pocock"
datum: 2026-10-16
erfasst: 2026-10-28
typ: youtube
quelle: youtube
status: verarbeitet
verarbeitet_am: 2026-10-28
source_notiz: 80_Knowledge/Sources/2026-10-16-matt-pocock-the-secret-to-building-robust-frontend-apps-with.md
video_id: "r8FYE2ZOj0E"
transkript_sprache: "de"
transkript_generiert: "ja"
transkript_segmente: "50"
transkript_zusatzsprache: "en"
transkript_zusatz_generiert: "ja"
transkript_zusatz_segmente: "46"
transkript_zusatz_datei: "medien/2026-10-16-matt-pocock-the-secret-to-building-robust-frontend-apps-with/transkript-youtube-en.json"
---

# The secret to building robust frontend apps with agents

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://www.youtube.com/watch?v=r8FYE2ZOj0E](https://www.youtube.com/watch?v=r8FYE2ZOj0E)

## Videobeschreibung

Learn why reducers are incredible for front-end development. Discover how separating UI logic from state management makes code more robust, testable, and maintainable.

Keep up to date with my skills here:

https://aihero.dev/s/1aIycd

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/EOsQ7j

## Transkript

Wissen Sie, was sich aus Frontend-Sicht absolut unglaublich anfühlt, wenn man mit Agenten, Reducern und Zustandsautomaten arbeitet? Ein Reducer sieht in etwa so aus. Er besitzt einen persistenten Zustand und dazu eine Reihe von Aktionen. Hier haben wir zum Beispiel „Kamera öffnen“, dann „ Kamera schließen“, „Foto aufgenommen“ usw. All diese Aktionen können durch das Frontend-UI ausgelöst werden. Das sind also Ereignisse, die durch Benutzeraktionen oder Fehler ausgelöst werden können. Der Reducer nimmt diese Aktionen entgegen und gibt einen neuen Zustand zurück. Auf einer sehr grundlegenden Ebene haben wir „Kamera öffnen“, was „Kamera offen: wahr“ zurückgibt, und „Kamera schließen “, was „Kamera offen: falsch“ zurückgibt. Das bewirkt etwas sehr, sehr Wichtiges: Es trennt die Benutzeroberfläche von der Logik, die diese Benutzeroberfläche steuert. Das bedeutet, dass diese Funktion, dieser Thumbnail-Zustands-Reducer, unabhängig außerhalb des Browsers getestet werden kann. Daher sind die Tests dafür sehr, sehr schnell. Wir sehen zum Beispiel auf der Thumbnail-Seite, wo wir einen Button mit „onClick-Dispatch: Kamera öffnen“ haben, dass die eigentliche Benutzeroberfläche sehr simpel ist.

Der React-Code ist sehr einfach gehalten. Mit anderen Worten: Wir konzentrieren einen Großteil der Logik für den Frontend-Code an einem einzigen Ort, der leicht zu testen, leicht zu ändern und leicht zu überblicken ist. Ich kann den Unterschied tatsächlich spüren, wenn ich mit einer Seite arbeite, die einen Reducer enthält, der von einem Agenten bearbeitet wurde. Das Ganze fühlt sich so viel robuster an, und es scheint, als seien die meisten Randfälle abgedeckt. Deshalb gehe ich gerade alte Projekte durch, an denen ich arbeite, und erhöhe die Anzahl der Reducer.

## Zusätzliches Transkript (Englisch)

> Zusätzlich direkt von YouTube erfasste englische Untertitelspur; automatisch erzeugt. Die oben archivierte deutsche Spur bleibt unverändert. [Unveränderter Segmentexport mit Zeitmarken](medien/2026-10-16-matt-pocock-the-secret-to-building-robust-frontend-apps-with/transkript-youtube-en.json).

You know what feels absolutely incredible to use from a front-end point of view when you're working with agents, reducers, and state machines. A reducer kind of looks like this. It's got some persistent state, and then it has a bunch of actions. So, here we've got open the camera, and then close the camera, and then photo captured, etc. All of these actions are things that can happen based on the front-end UI. So, these are events that could trigger based on user actions or things failing, etc. And then all the reducer does is it takes in those actions and returns a new state. So, on a very basic level, you've got open camera, which returns open camera true, and then close camera, which returns open camera open false.

Now, this does something very, very important, which is it separates the user interface from the logic that controls that user interface. That means that this function, this thumbnail state reducer, what it can do, it can be tested independently outside of the browser. So, the tests for it are very, very fast. And we can see, for instance, in the thumbnails page where we have a button on click dispatch open camera, it means that the actual user interface is very stupid. The React code is very dumb. In other words, we're concentrating a lot of the logic for the front-end code in a single place that's easy to test, easy to modify, and easy to see the entire thing of how it all works together. And so, I can actually feel the difference when I work with a page that has a reducer in it that an agent has edited. The whole thing just feels so much more robust, and it feels like most of the edge cases are handled.

So, I'm actually going back over old projects that I'm working on and cranking up the number of reducers.
