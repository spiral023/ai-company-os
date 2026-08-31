---
url: https://www.tiktok.com/@agentic.james/video/7671088367332838670
autor: "@agentic.james"
datum: 2026-08-07
erfasst: 2026-08-31
typ: video
quelle: tiktok
status: neu
titel: "Most people think context engineering is some complex art."
video_id: "7671088367332838670"
transkript: automatisch
laenge: "02:29"
sprache: en
---

# Most people think context engineering is some complex art.

![Cover](medien/2026-08-07-agenticjames-most-people-think-context-engineering-is-some-complex-art/01-cover.jpg)

## Caption

Most people think context engineering is some complex art. It really isn't. Your coding agent is just an LLM with a context window, and a harness like Claude Code overlays a system prompt and tool definitions you can't touch. The whole game is that anything that doesn't reach the context window literally does not exist to your agent. So your CLAUDE.md or agents.md file is the trunk, it loads automatically every single time, and from there you point to skills, scripts, MCP tools, and workflows like branches on a tree. Your agent follows the breadcrumbs out to the leaves and only loads what the task actually needs. That's progressive disclosure, and it's how you give an agent access to a hundred tools without drowning it in context up front. Get this one mental model and everything else about agent context clicks.

## Transkript

Here's everything you need to know about context engineering for coding agents in one minute. First of all, in the background, all a coding agent is is an LLM with inputs and outputs, and the limit to those inputs is the context window. On top of that LLM, in the background, there is a harness like Claude code that allows that LLM to use tools. There are short definitions of these tools that get included in every prompt that you send to your coding agent, as well as a system prompt that tells your coding agent how to behave that you cannot change. You can't edit any of this getting to your coding agent's context window. But on top of this is where context engineering comes into play. We can take inspiration from the way that these companies have designed coding agents with system prompts and tool definitions sent into the context window to overlay your own custom instructions, tools, and workflows into the context window on top of theirs. The important part to realize is that what doesn't reach your agent's context window, it does not know about. So you want to leverage something like a claw dot MD file or an agent's dot MD file as the entry point into all of the tools or workflows that you want your agent to perform. This is because these files are automatically loaded into your agent's context window just like the system prompt, except you can edit them once you Realize these documents are the entry point into your ability to context engineer your coding agent. You can point to different files or workflows within that claw dot MD or agents dot MD file, like a skilled workflow or a separate MCP tool to instruct your agent exactly how to use them. From this point on, you should think of context engineering like a branching tree, the trunk being your agents or claw dot MD file that's automatically loaded into context so your agent will always know about it. And then you give your agent decisions from that claw dot MD file that point to different folders and files throughout your code base, and you allow it to make decisions on which folders or files to load from that point to do what you're asking it. These different decisions represent the branches of the tree and they can contain documents, scripts, workflows, skills, and MCP tools. This concept of giving your agent decisions to choose what files and folders and tools to load is called progressive disclosure, it's the way to allow your agent to have access to a bunch of tools, resources, and workflows with without loading all of it into context window at the start. Because the core of all of it is stored in the claw dot MD file, and your coding agent can follow the breadcrumbs from that trunk out to the leaves for whatever specific task it needs to complete. As long as you Point to the branches and leaves further out on the tree. Your coding agent will know to traverse to the correct location to load the correct context into its context window for whatever task it's completing for you. Do you wanna be a top 1% coding agent user and get really good at context engineering? I host full video courses on all these topics in my school community. The link is in my bio and we would love to see you there.
