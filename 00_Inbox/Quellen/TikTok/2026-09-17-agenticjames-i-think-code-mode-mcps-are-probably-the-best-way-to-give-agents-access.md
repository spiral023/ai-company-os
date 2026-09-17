---
url: https://www.tiktok.com/@agentic.james/video/7686584043177135373
autor: "@agentic.james"
datum: 2026-09-17
erfasst: 2026-09-17
typ: video
quelle: tiktok
status: neu
titel: "I think code mode MCPs are probably the best way to give agents access to tools."
video_id: "7686584043177135373"
hashtags: "mcp, aiautomation, claudecode, codex, aiagents"
transkript: automatisch
laenge: "01:37"
sprache: en
---

# I think code mode MCPs are probably the best way to give agents access to tools.

![Cover](medien/2026-09-17-agenticjames-i-think-code-mode-mcps-are-probably-the-best-way-to-give-agents-access/01-cover.jpg)

## Caption

I think code mode MCPs are probably the best way to give agents access to tools. Like MCP and CLI had a baby.

## Transkript

You're still using normal M C P servers and C L I. Tools. You should really try code mode M C P. Let me explain a few of the reasons why I think this is the best way to give agents access to tools. No.1. It makes all of your M C P tools composable, which means your agent can dynamically generate the specific type of M C P tool call that it wants to make for that specific purpose. A code mode M C P basically exposes one M C P tool that allows the agent to execute a script that dynamically calls all of your other M C P tools once it's executed. First your agent can search for all the M C P tools that it wants to call, and then it can generate a custom script to call multiple tools at the same time with one M C P tool call. And even generate that script to filter the output so a huge Jason body doesn't flood its context window. This brings me to my second point, which is context consumption reduction. Because your agent can dynamically generate a custom tool for everything that it wants to do, it can also filter how the outputs of that tool reach its context window. Instead of what we see at the top. Like a traditional M C P server that has pre defined tools that the agent can't really filter the output from, it dynamically generates the Shape of that tool. This is similar to how C L I. Tools work in that it's composable, but it also has the added benefit of being an M C P tool itself. So it has its tool description loaded into your agent's context window automatically, so it knows it's there to use. There's a bunch of different code mode M C P gateways. I know Docker has one, but I use the executor M C P gateway. Allows me to log into all my M C P servers and use all of them as a code mode M C P behind the executor tool. This tool is super cool. Completely free, self hostable. I just recorded a full 30 minute tutorial on how to set it up for yourself, your team members, all that good stuff if you wanna watch that. It's hosted in my school community. Link in bio. Would love to see you there!
