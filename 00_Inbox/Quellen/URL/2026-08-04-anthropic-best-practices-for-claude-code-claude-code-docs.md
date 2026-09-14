---
url: https://www.anthropic.com/engineering/claude-code-best-practices
titel: "Best practices for Claude Code - Claude Code Docs"
autor: "Claude Code Docs"
datum: 2026-08-04
datum_unsicher: true
erfasst: 2026-08-04
typ: url
quelle: url
status: verarbeitet
verarbeitet_am: 2026-08-05
source_notiz: 80_Knowledge/Sources/2026-08-04-anthropic-docs-claude-code-best-practices.md
---

# Best practices for Claude Code - Claude Code Docs

> Automatisch per `python 70_Scripts/ingest_source.py` erfasst. Quelle: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

## Inhalt

## Best practices for Claude Code

Tips and patterns for getting the most out of Claude Code, from configuring your environment to scaling across parallel sessions.

### ​ Give Claude a way to verify its work

- In one prompt : ask Claude to run the check and iterate in the same message, as in the table above.

- Across a session : set the check as a /goal condition . A separate evaluator re-checks it after every turn and Claude keeps working until it holds.

- As a deterministic gate : a Stop hook runs your check as a script and blocks the turn from ending until it passes. Claude Code overrides the hook and ends the turn after 8 consecutive blocks.

- By a second opinion : a verification subagent or a dynamic workflow that checks its own findings has a fresh model try to refute the result, so the agent doing the work isn’t the one grading it.

### ​ Explore first, then plan, then code

Explore

```
read /src/auth and understand how we handle sessions and login.
also look at how we manage environment variables for secrets.

```

Plan

```
I want to add Google OAuth. What files need to change?
What's the session flow? Create a plan.

```

Implement

```
implement the OAuth flow from your plan. write tests for the
callback handler, run the test suite and fix any failures.

```

Commit

```
commit with a descriptive message and open a PR

```

### ​ Provide specific context in your prompts

#### ​ Provide rich content

- Reference files with @ instead of describing where code lives. Claude reads the file before responding.

- Paste images directly . Copy/paste or drag and drop images into the prompt.

- Give URLs for documentation and API references. Use /permissions to allowlist frequently-used domains.

- Pipe in data by running cat error.log | claude to send file contents directly.

- Let Claude fetch what it needs . Tell Claude to pull context itself using Bash commands, MCP tools, or by reading files.

### ​ Configure your environment

#### ​ Write an effective CLAUDE.md

```
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance

```

```
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md

```

- Home folder ( ~/.claude/CLAUDE.md ) : applies to all Claude sessions

- Project root ( ./CLAUDE.md ) : check into git to share with your team

- Project root ( ./CLAUDE.local.md ) : personal project-specific notes; add this file to your .gitignore so it isn’t shared with your team

- Parent directories : useful for monorepos where both root/CLAUDE.md and root/foo/CLAUDE.md are pulled in automatically

- Child directories : Claude pulls in child CLAUDE.md files on demand when it reads a file in those directories

#### ​ Configure permissions

- Auto mode : a separate classifier model reviews commands and blocks only what looks risky: scope escalation, unknown infrastructure, or hostile-content-driven actions. Best when you trust the general direction of a task but don’t want to click through every step

- Permission allowlists : permit specific tools you know are safe, like npm run lint or git commit

- Sandboxing : enable OS-level isolation that restricts filesystem and network access, allowing Claude to work more freely within defined boundaries

#### ​ Use CLI tools

#### ​ Connect MCP servers

#### ​ Set up hooks

#### ​ Create skills

```
---
name: api-conventions
description: REST API design conventions for our services
---
# API Conventions
- Use kebab-case for URL paths
- Use camelCase for JSON properties
- Always include pagination for list endpoints
- Version APIs in the URL path (/v1/, /v2/)

```

```
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR

```

#### ​ Create custom subagents

```
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling

Provide specific line references and suggested fixes.

```

#### ​ Install plugins

### ​ Communicate effectively

#### ​ Ask codebase questions

- How does logging work?

- How do I make a new API endpoint?

- What does async move { ... } do on line 134 of foo.rs ?

- What edge cases does CustomerOnboardingFlowImpl handle?

- Why does this code call foo() instead of bar() on line 333?

#### ​ Let Claude interview you

```
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.

```

### ​ Manage your session

#### ​ Course-correct early and often

- Esc : stop Claude mid-action with the Esc key. Context is preserved, so you can redirect.

- Esc + Esc or /rewind : press Esc twice or run /rewind to open the rewind menu and restore previous conversation and code state, or summarize from a selected message.

- "Undo that" : have Claude revert its changes.

- /clear : reset context between unrelated tasks. Long sessions with irrelevant context can reduce performance.

#### ​ Manage context aggressively

- Use /clear frequently between tasks to reset the context window entirely

- When auto compaction triggers, Claude summarizes what matters most, including code patterns, file states, and key decisions

- For more control, run /compact <instructions> , like /compact Focus on the API changes

- To compact only part of the conversation, use Esc + Esc or /rewind , select a message checkpoint, and choose Summarize from here or Summarize up to here . The first condenses messages from that point forward while keeping earlier context intact; the second condenses earlier messages while keeping recent ones in full. See the rewind menu’s summarize options .

- Customize compaction behavior in CLAUDE.md with instructions like "When compacting, always preserve the full list of modified files and any test commands" to ensure critical context survives summarization

- For quick questions that don’t need to stay in context, use /btw . The answer appears in a dismissible overlay and never enters conversation history, so you can check a detail without growing context.

#### ​ Use subagents for investigation

```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.

```

```
use a subagent to review this code for edge cases

```

#### ​ Rewind with checkpoints

#### ​ Resume conversations

### ​ Automate and scale

#### ​ Run non-interactive mode

```
# One-off queries
claude -p "Explain what this project does"

# Structured output for scripts
claude -p "List all API endpoints" --output-format json

# Streaming for real-time processing
claude -p "Analyze this log file" --output-format stream-json --verbose

```

#### ​ Run multiple Claude sessions

- Worktrees : run separate CLI sessions in isolated git checkouts so edits don’t collide

- Desktop app : manage multiple local sessions visually, each in its own worktree

- Claude Code on the web : run sessions on Anthropic-managed cloud infrastructure in isolated VMs

- Agent teams : automated coordination of multiple sessions with shared tasks, messaging, and a team lead

#### ​ Fan out across files

Generate a task list

Write a script to loop through the list

```
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done

```

Test on a few files, then run at scale

```
claude -p "<your prompt>" --output-format json | your_command

```

#### ​ Run autonomously with auto mode

```
claude --permission-mode auto -p "fix all lint errors"

```

#### ​ Add an adversarial review step

```
Use a subagent to review the rate limiter diff against PLAN.md. Check that
every requirement is implemented, the listed edge cases have tests, and
nothing outside the task's scope changed. Report gaps, not style preferences.

```

### ​ Avoid common failure patterns

- The kitchen sink session. You start with one task, then ask Claude something unrelated, then go back to the first task. Context is full of irrelevant information. Fix : /clear between unrelated tasks.

> Fix : /clear between unrelated tasks.

- Correcting over and over. Claude does something wrong, you correct it, it’s still wrong, you correct again. Context is polluted with failed approaches. Fix : After two failed corrections, /clear and write a better initial prompt incorporating what you learned.

> Fix : After two failed corrections, /clear and write a better initial prompt incorporating what you learned.

- The over-specified CLAUDE.md. If your CLAUDE.md is too long, Claude ignores half of it because important rules get lost in the noise. Fix : Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.

> Fix : Ruthlessly prune. If Claude already does something correctly without the instruction, delete it or convert it to a hook.

- The trust-then-verify gap. Claude produces a plausible-looking implementation that doesn’t handle edge cases. Fix : Always provide verification (tests, scripts, screenshots). If you can’t verify it, don’t ship it.

> Fix : Always provide verification (tests, scripts, screenshots). If you can’t verify it, don’t ship it.

- The infinite exploration. You ask Claude to “investigate” something without scoping it. Claude reads hundreds of files, filling the context. Fix : Scope investigations narrowly or use subagents so the exploration doesn’t consume your main context.

> Fix : Scope investigations narrowly or use subagents so the exploration doesn’t consume your main context.

### ​ Develop your intuition

### ​ Related resources

- How Claude Code works : the agentic loop, tools, and context management

- Extend Claude Code : skills, hooks, MCP, subagents, and plugins

- Common workflows : step-by-step recipes for debugging, testing, PRs, and more

- CLAUDE.md : store project conventions and persistent context

Was this page helpful?
