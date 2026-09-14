---
url: https://code.claude.com/docs/en/plugin-evals
titel: "Test plugins with evals - Claude Code Docs"
autor: "Claude Code Docs"
datum: 2026-09-14
erfasst: 2026-09-14
typ: url
quelle: url
status: neu
medien: "1/1 lokal"
---

# Test plugins with evals - Claude Code Docs

> Automatisch per `python ai.py ingest` erfasst. Quelle: [https://code.claude.com/docs/en/plugin-evals](https://code.claude.com/docs/en/plugin-evals)

## Inhalt

## Test plugins with evals

Write eval cases for your Claude Code plugin, run them with claude plugin eval, grade the results, compare against a no-plugin baseline, and gate CI on the score.

### ​ Requirements

- Claude Code v2.1.269 or later. Run claude --version to check and claude update to upgrade.

- A plugin directory with a plugin.json or .claude-plugin/plugin.json manifest, or a skills-directory plugin .

- The same authentication and model provider your normal Claude Code sessions use. Eval runs, judge-scored graders, and claude plugin eval init call the model with your credentials, so they count against your plan’s usage limits or your API bill. When the command reports a cost, the figure is a list-price estimate of those calls.

### ​ How an eval run works

#### ​ What happens in a run

#### ​ How a case is scored

#### ​ The no-plugin baseline

### ​ Create your first eval suite

- Claude Code v2.1.269 or later and the other requirements

- A terminal open at your plugin’s root directory, the one containing plugin.json or .claude-plugin/plugin.json

- One skill in the plugin you want to test, and a request a user would type that should trigger it

Create the cases

```
claude plugin eval init

```

Run the suite

```
claude plugin eval .

```

Read the summary

```
CASE        WITH  W/OUT Δ      RUNS COST    NOTES
first-case  1.00  0.33  +0.67  6    $0.41

1 case(s) · mean Δ +0.67 · 74s · $0.41
Report: /Users/you/my-plugin/evals/results/2026-09-10T17-02-11-482Z/report.html
Published: https://claude.ai/... · keep local next time with --no-publish

```

Open the report and iterate

```
claude plugin eval . --case <case-name> --runs 1 --ablation none

```

### ​ Write and refine cases

```
my-plugin/
├── .claude-plugin/plugin.json
├── skills/...
└── evals/
    ├── first-case/
    │   ├── prompt.md          # frontmatter: case fields; body: the prompt
    │   ├── graders/
    │   │   ├── criteria.md    # frontmatter: type + options; body: rubric or pattern
    │   │   └── skill-fired.md
    │   └── case.yaml          # optional: only for context.* fields
    ├── ignores-unrelated-request/
    │   └── ...
    └── results/               # written by each run; add to .gitignore

```

#### ​ Write a case manually

```
claude plugin eval init --bare first-case

```

```
evals/first-case/
├── prompt.md            # the prompt sent to Claude, plus run limits
└── graders/
    └── criteria.md      # one grader: how to score the result

```

```
---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

Write me a commit message for this change: I renamed getUser to fetchUser and updated the three call sites.

```

```
---
type: llm
---

PASS if <what a correct response contains>.
FAIL if <what a wrong or missing response looks like>.

```

```
---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?your-skill-name"'
---

```

#### ​ Set run limits and tools in prompt.md

#### ​ Choose and weight graders

##### ​ Choose graders that give a stable signal

- For long output such as a generated file, grade it with a regex grader over the file’s contents, which checks the whole file the same way every time. Keep llm graders for short outputs, with rubrics written as concrete PASS and FAIL conditions.

- Give each case one grader on the result, such as the final message or a produced file, and one on how Claude got there, such as tool_used or tool_order . Together they tell you both whether the answer was right and whether your plugin produced it.

- If a case’s tool_used: Skill grader passes but Δ is negative, suspect the judge before the plugin. A small judge model can mark a correct answer wrong because it’s formatted differently from what the rubric describes. Re-run with --judge-model sonnet , and tighten the rubric so formatting doesn’t decide the verdict.

- To check that a build or test passed inside the run, have the prompt ask Claude to run it and write the outcome to a file, grade that file, and assert the command ran with a tool_used grader whose input_match names the command.

#### ​ Score against the no-plugin baseline

- Every tool_used grader whose tool is Skill

- Any grader you mark arm: with-only

#### ​ Use a different eval directory

- In plugin.json : add "experimental": { "evals": "quality/evals" } .

- On the command line : pass --eval-dir quality/evals to both claude plugin eval and claude plugin eval init .

### ​ Set up fixtures and mocks

#### ​ Seed the workspace or conversation

```
schema_version: "1.1"
name: changelog-from-diff
tags: [smoke]
context:
  scaffold_script: fixture.sh
  add_dirs: [resources]

```

#### ​ Mock MCP servers

```
---
expect:
  title: string
  priority: [low, medium, high]
---

Created issue #4821: {{input.title}}

```

- --allow-real-servers : start the real process for each server you haven’t mocked, and keep answering mocked tools from their files

- --mocks off : ignore mocks/ entirely and start every server the plugin declares

##### ​ Replay agent mock answers

### ​ Run evals

#### ​ Choose what to evaluate

#### ​ Grant tools

```
claude plugin eval . --allow-tools Write Edit "Bash(npm test *)"

```

#### ​ Command options

#### ​ Run evals in CI

```
claude plugin eval . \
  --trust-plugin \
  --json results.json \
  --threshold 0.8 \
  --model claude-sonnet-5 \
  --judge-model claude-haiku-4-5 \
  --no-publish \
  --max-cost-usd 20

```

### ​ Read the results

#### ​ HTML report

- The verdict line and tiles answer whether the plugin helped across the whole suite. Suite score is the mean of the per-case with-plugin scores, Ablation Δ is how far that sits above or below the baseline score, and Cases counts how many met the threshold. Perfect runs is the share of with-plugin runs where every grader passed.

- Each case card shows the case’s own Δ and with-plugin score, with a tick on the bar at the threshold. A case whose Δ is negative gets a red left edge, so regressions stand out when you scroll.

- Inside a case , the with-plugin runs come first and the baseline runs after. Each run lists its graders with a pass or fail chip. A failed grader is already expanded with its explanation, and an llm grader also shows the judge’s votes and the evidence it was shown, which is where you find out why a run scored low. Graders that don’t count toward the score, such as tool_used: Skill , carry a plugin-fired indicator badge.

- Prompt and Graders , below the runs, show the case’s prompt and each grader’s rubric or pattern, so someone reading the report without the suite can see what was asked and what counted as good.

#### ​ JSON result

### ​ What a run can access

#### ​ Trust the plugin directory

#### ​ How runs are isolated

- Nothing personal or project-level loads. Your user settings, hooks, CLAUDE.md files, MCP servers, other installed plugins, memory, and skills are absent, and no project-scoped .claude/ or .mcp.json above the sandbox is read. Most of your shell environment is withheld too; only an allowlist and EVAL_* variables reach the run. If the plugin needs setup, ship it in the plugin, create it in a scaffold_script , or pass EVAL_* variables.

- Managed policy can still restrict a run. Restrictions in managed settings an administrator deployed to the machine apply inside a run, so results on a managed machine can differ from an unmanaged one by that policy.

- The Artifact tool is off. A skill that publishes an artifact can be graded only on what it produces before that step.

- The case definitions are hidden from the agent. A run can’t read the eval directory, so Claude can’t see the case’s prompt, its graders, or sibling cases.

- No network sandbox outside shell commands. Shell commands you grant run under the sandbox’s network rules. A WebFetch(domain:…) grant reaches that domain directly, and the plugin’s own hooks and any real MCP servers you start can reach any host.

### ​ Eval suite reference

```
evals/
├── <case>/                        # one directory per case; nest under a non-case directory to group
│   ├── prompt.md                  # frontmatter: case and run fields; body: the prompt
│   ├── case.yaml                  # optional: context.* fields, or the whole case in one file
│   ├── graders/
│   │   └── <name>.md              # one grader per file; frontmatter: type and options; body: rubric
│   ├── mocks/                     # optional: mocks for this case only, same layout as below
│   └── <fixtures, scripts, transcripts referenced by case.yaml>
├── mocks/                         # optional: suite-wide MCP mocks
│   ├── <server>/
│   │   ├── <tool>.md              # one mocked tool; body: the tool result
│   │   ├── _server.md             # optional: one agent that answers several tools
│   │   ├── _tools.json            # optional: saved tools/list response for real descriptions and schemas
│   │   └── fixtures/              # files inserted with {{file:fixtures/...}}
│   └── .replay/<server>/          # adopted agent-mock recordings, answered without a model call
└── results/<timestamp>/           # written by each run; add results/ to .gitignore
    ├── aggregate-result.json
    ├── report.html
    └── mock-recordings/           # agent-mock answers from clean runs, with ADOPT.txt

```

#### ​ prompt.md frontmatter

#### ​ case.yaml fields

#### ​ Grader frontmatter

##### ​ What a grader can look at

##### ​ Grader types

#### ​ Mock files

- _server.md : a single type: agent mock that answers several tools, listed in its tools: frontmatter key. A <tool>.md for the same tool takes precedence. Put an expect: guard on the individual <tool>.md , not here

- _tools.json : a saved tools/list response from the real server, so mocked tools carry their real descriptions and input schemas instead of a permissive placeholder

### ​ Troubleshooting

#### ​ ”plugin eval is currently in early access”

#### ​ ”plugin eval is currently unavailable”

#### ​ ”is not a trusted plugin directory, and this run cannot stop to ask you about it”

#### ​ ”No eval cases found”

#### ​ The baseline arm shows no plugin, or delta is zero

#### ​ Everything scores zero although the right files were produced

#### ​ A regex over the trace doesn’t match text I can see

#### ​ Tools are denied, MCP tools are missing, or Bash won’t run

#### ​ The run exits 1 but the results look fine

#### ​ ”—json output path must end in .json”

#### ​ A grader shows passed: false under a run that scored 1.0

#### ​ Runs fail with a usage-limit or rate-limit error partway through

#### ​ Runs time out or hit the turn cap

### ​ See also

- Create plugins : build the plugin you’re testing, and load it with --plugin-dir during development

- Plugins reference : the plugin eval and plugin eval init command entries and the manifest’s experimental.evals key

- Skills : how a skill’s description decides when Claude invokes it, which is what a case that checks whether the skill triggers is measuring

- Sandboxing : the OS-level sandbox that applies when you grant Bash to a run

- Create and distribute a plugin marketplace : publish the plugin once its suite passes

Was this page helpful?

## Bilder

![Top of an eval report: a verdict line reading "Plugin effect: +33.3 pts vs baseline, improved 2, flat 1, regressed 0 of 3 cases", five summary tiles for suite score, ablation delta, baseline score, cases passing the threshold, and perfect runs, then the first case with its delta, score bar, and one run whose two graders both show pass](medien/2026-09-14-code-test-plugins-with-evals-claude-code-docs/01-bild.png)
