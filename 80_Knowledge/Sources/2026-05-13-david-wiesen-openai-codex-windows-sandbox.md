---
url: https://openai.com/index/building-codex-windows-sandbox/
autor: David Wiesen
datum: 2026-05-13
erfasst: 2026-08-04
typ: artikel
rohquelle: 00_Inbox/Quellen/2026-05-13-david-wiesen-openai-codex-windows-sandbox.md
beleg_art: sekundaerquelle
---

# Wie OpenAI Codex' Windows-Sandbox aus mehreren OS-Primitiven zusammensetzte

Während [[2026-02-28-openai-codex-rules-guide]] beschreibt, welche Befehle Codex außerhalb der Sandbox ausführen darf, beschreibt dieser Artikel, wie die Sandbox-Grenze selbst auf Windows überhaupt entsteht. Beides sind unterschiedliche Ebenen desselben Systems: Rules ist Codex-Konfiguration (portabel, anwendungsseitig), die Windows-Sandbox ist Betriebssystem-Mechanik (plattformspezifisch, tief in Windows-APIs). Es gibt zwischen beiden Quellen keinen Widerspruch, nur eine klare Arbeitsteilung.

## Warum die naheliegenden Windows-Mechanismen nicht reichten

OpenAI prüfte drei native Windows-Sandbox-Ansätze und verwarf alle: **AppContainer** ist für Anwendungen gedacht, die ihren Zugriffsbedarf vorab kennen — Codex muss aber Shells, Git, Python, Build-Tools und beliebige weitere Binaries ansteuern, also einen offenen statt statisch definierten Arbeitskontext. **Windows Sandbox** bietet eine starke VM-Grenze, trennt Codex aber vom realen Checkout und Tooling des Nutzers ab und ist zudem nicht auf allen Windows-Editionen verfügbar. **Mandatory Integrity Control** hätte den echten Workspace des Entwicklers semantisch in einen für alle Low-Integrity-Prozesse offenen Bereich verwandelt, nicht nur für Codex — zu breit für einen produktiven Checkout.

## Der erste Prototyp: unelevated Sandbox über SIDs und restricted Tokens

Der erste Ansatz kam ohne Admin-Rechte aus. Für Filesystem-Writes kombinierte OpenAI eine synthetische SID (`sandbox-write`) mit write-restricted Process Tokens: Die SID erhält Write-/Execute-/Delete-Rechte auf das Working Directory und zusätzliche `writable_roots`, wird aber explizit von sensiblen Unterpfaden wie `.git`, `.codex` und `.agents` ausgeschlossen. Codex startet Kommandos unter einem Token, dessen restricted SID list `Everyone`, die aktuelle Logon-Session und `sandbox-write` enthält — ein Write gelingt nur, wenn sowohl der normale Nutzerkontext als auch mindestens eine passende restricted SID Zugriff haben.

Das eigentliche Problem lag laut OpenAI nicht beim Filesystem, sondern beim Netzwerk: Der erste Netzwerkschutz war rein **advisory** (Proxy-Umgebungsvariablen) und ließ sich von Programmen umgehen, die diese ignorieren oder einen eigenen Socket-Stack nutzen — zu schwach sowohl gegen feindlichen als auch gegen gutwilligen, aber nicht kooperativen Code.

## Warum Windows Firewall die Architektur veränderte

Windows Firewall wäre der naheliegende Kandidat für durchsetzende Netzwerkkontrolle gewesen, aber Firewall-Regeln ließen sich nicht an die non-principal identity einer restricted SID binden. Binary-basierte Regeln hätten nur `codex.exe`, nicht aber Kindprozesse wie `python.exe` oder `git.exe` erfasst; user-scoped Regeln hätten den echten Windows-User getroffen statt nur den sandboxed Process Tree. Konsequenz: Ein pro Sandbox-Prozessbaum steuerbarer Netzwerkzugriff braucht einen eigenen Principal.

## Die elevated Sandbox: zwei neue Windows-User

Der Redesign-Kern: Der restricted Token bleibt, aber sein Principal ist nicht mehr der reale Windows-User, sondern einer von zwei eigens angelegten lokalen Nutzern — `CodexSandboxOffline` (von Firewall-Regeln getroffen) und `CodexSandboxOnline` (nicht getroffen). Das erfordert einmalig Admin-Rechte beim Setup, das dafür synthetische SID und Sandbox-User anlegt, deren Credentials per DPAPI verschlüsselt lokal speichert und Firewall-Regeln für `CodexSandboxOffline` validiert. Damit die Sandbox-User möglichst ähnliche Leserechte wie der echte Nutzer haben, vergibt das Setup zusätzliche Read-ACLs auf Pfade wie `C:\Users\<real-user>`, `C:\Windows\`, `C:\Program Files\` und `C:\ProgramData\` — diese ACL-Arbeit läuft teilweise asynchron, um den blockierenden Setup-Schritt nicht unnötig zu verlangsamen.

Die Setup-Logik liegt in einem eigenen Binary (`codex-windows-sandbox-setup.exe`), damit `codex.exe` selbst unelevated bleibt und Windows-spezifischer Code die Hauptbinary auf anderen Plattformen nicht aufbläht. Weil ein separater Sandbox-User keinen restricted Token mehr direkt vom echten Nutzerkontext aus für den finalen Kindprozess bauen kann (Privileggrenze um `CreateProcessAsUserW`), gibt es zusätzlich einen `codex-command-runner.exe`: `codex.exe` startet ihn per `CreateProcessWithLogonW` als Sandbox-User, und erst innerhalb dieses Runners wird per `GetTokenInformation` und `CreateRestrictedToken` der finale restricted Token gebaut, mit dem `CreateProcessAsUserW` den eigentlichen Kindprozess startet. Die finale Architektur besteht damit aus vier Schichten: `codex.exe`, `codex-windows-sandbox-setup.exe`, `codex-command-runner.exe` und dem eigentlichen Kindprozess.

## Einordnung

Dies ist ein OpenAI-Engineering-Post in sekundärer deutscher Aufarbeitung — die beschriebene API-Sequenz (SIDs, restricted Tokens, `CreateProcessAsUserW` usw.) ist OpenAIs Selbstauskunft über die eigene Architektur, hier nicht gegen den Quellcode von Codex nachgeprüft. Der Wert liegt weniger in den Windows-API-Details (versionsabhängig, für die meisten Leser nicht direkt nachbaubar) als im übertragbaren Architekturprinzip: Kein einzelnes natives OS-Feature deckte den Bedarf eines Coding Agents ab, die Sandbox musste aus mehreren Primitiven komponiert werden (ACLs, restricted Tokens, synthetische SIDs, eigene lokale User, Firewall-Regeln, DPAPI, separate Hilfsbinaries). Die durchgehende Spannung — harte Durchsetzung vs. realistischer Entwickler-Workflow — ist eine Designfrage, die sich auf jede Agent-Sandbox-Architektur übertragen lässt, nicht nur auf Windows. Das deckt sich mit dem bereits im Bestand notierten Punkt, dass Container-Isolation für viele Projekte zu aufwendig ist ([[Deny-Rules-statt-CLAUDE-md-Empfehlung]], Nachteile), liefert dafür aber erstmals die technische Begründung, warum eine schwächere, rein advisory Lösung (hier: Netzwerk per Proxy-Variable) nicht ausreicht.

## Kernaussagen

- Kein einzelnes natives Windows-Feature (AppContainer, Windows Sandbox, MIC) passte auf den Bedarf eines offenen Agent-Workflows; die Sandbox musste aus mehreren OS-Primitiven komponiert werden → [[Sandbox-Komposition-aus-OS-Primitiven]]
- Advisory Netzwerkschutz (Proxy-Umgebungsvariablen) ließ sich von nicht kooperativem oder feindlichem Code umgehen; erst eine durchsetzende, an einen eigenen Principal gebundene Firewall-Regel schließt die Lücke → [[Deny-Rules-statt-CLAUDE-md-Empfehlung]] (bestätigt „Empfehlung ≠ Durchsetzung“ auf Netzwerkebene statt Dateiebene)
- Die zentrale Spannung jeder Architekturentscheidung im Artikel ist harte Durchsetzung vs. realistischer Entwickler-Workflow, nicht Security als Selbstzweck → [[Sandbox-Komposition-aus-OS-Primitiven]]
- Ein separates, unelevated Haupt-Binary plus dediziertes Setup-Binary trennt einmaligen Admin-Bedarf von der täglichen Nutzung — eine Architekturentscheidung auch aus Wartbarkeitsgründen, nicht nur Security

## Verbindungen

- [[Deny-Rules-statt-CLAUDE-md-Empfehlung]]
- [[2026-02-28-openai-codex-rules-guide]]
- [[Sandbox-Komposition-aus-OS-Primitiven]]
