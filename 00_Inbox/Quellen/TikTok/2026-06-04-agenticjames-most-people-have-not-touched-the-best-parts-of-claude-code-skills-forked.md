---
url: https://www.tiktok.com/@agentic.james/video/7647517398890794253
autor: "@agentic.james"
datum: 2026-06-04
erfasst: 2026-08-31
typ: video
quelle: tiktok
status: neu
titel: "Most people have not touched the best parts of Claude Code skills: forked …"
video_id: "7647517398890794253"
transkript: automatisch
laenge: "01:55"
sprache: en
---

# Most people have not touched the best parts of Claude Code skills: forked …

![Cover](medien/2026-06-04-agenticjames-most-people-have-not-touched-the-best-parts-of-claude-code-skills-forked/01-cover.jpg)

## Caption

Most people have not touched the best parts of Claude Code skills: forked context windows with their own model, $ARGUMENTS for parameterized slash commands, and descriptions written so the skill actually triggers. Getting these right is the difference between skills that sit unused and skills that fire every time. I wrote up the full guide on creating skills correctly plus the 7 I would install first. Comment SKILLS and I will send it over.

## Transkript

You're still missing so many cool features of Claude Code skills. The biggest one people don't use is that there's a fork parameter in the YAML front matter of a skill that basically allows Claude Code to run that skill in a forked separate context window in a subagent with a different model. This gives you way better control over the amount of tokens that are consumed depending on what type of work your agent is working on. For instance, if you want to run a Sonic session, but when it does an architecture review of a lot of code, you want to use Opus. You can use an architecture review skill with a forked context window and model set to Opus so that Opus is only used for that skill. You can define this in your skills as is shown here with context set to fork and model set to Opus. The second thing I don't see people using a lot is the arguments variable, which allows you to actually pass in extra information before you're calling a specific skill. Basically allows you to invoke a skill like slash DOCX and then put a space after it and actually pass in extra information about maybe what file you want turned into a docx file. To enable this in your skill, you just have to write the dollar sign arguments variable in the actual skill file, and whatever you pass in after you invoke that skill with the slash command Will actually replace this variable when code calls it. The third thing is the prompting style of writing the description and triggers of a skill. This is how code knows when to use that skill correctly. Description is at the top of the YAML front matter in your skill, and you want this to be an imperative voice. You really want to instruct Claude code. You must use this skill when blank. And the triggers basically define specific trigger words that will trigger Claude code to use that skill in addition to the description. Using all these techniques when you're building skills with Claude Code will greatly increase the amount that Claude Code actually uses your skill correctly and the outputs that you get from those skills. So if you want the full guide of all the details of how to create skills correctly, just comment skills below and I'll send it over. I cover all of the Claude Code features in this much detail in my Claude Code Fundamentals course, which is hosted in my school community. We have 550 members contributing to this as well as a full multi agent Claude code system, so if you're interested in that, hit the link in bio and I'd love to see you there.
