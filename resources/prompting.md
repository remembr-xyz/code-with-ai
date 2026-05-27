# Prompting

> **TL;DR** Most underrated skill in this stack. Read 3 leaked system prompts before you write your own. The named patterns below cover 90% of what you'll do day-to-day. Anthropic's prompt library is the best free resource.

The most underrated skill in this whole stack. A great `AGENTS.md` plus great prompts is more valuable than a fancier model.

## Curated prompt libraries

### [Anthropic prompt library](https://docs.anthropic.com/claude/prompt-library)
Sortable by use case. Production-ready prompts for summarization, classification, extraction, code review, more. The single best starting point.

### [OpenAI Cookbook](https://cookbook.openai.com)
Recipes, not just prompts. Function-calling patterns, RAG, evals, agent loops. Treat it as a textbook.

### [The Prompting Guide](https://promptingguide.ai)
Long-form free guide. Covers chain-of-thought, ReAct, tree-of-thoughts, the techniques that became standard. Less hand-holdy than other tutorials.

### [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
The OG community prompt collection. Personas, tasks, formats. Some are dated; the patterns aren't.

## Look at the leaked ones

The fastest way to learn what good prompting looks like is to read the system prompts of the tools you already use. People have leaked or reverse-engineered most of them.

### [`system_prompts_leaks`](https://github.com/asgeirtj/system_prompts_leaks)
Cursor, Claude Code, GitHub Copilot, v0, Devin, ChatGPT, more. Updated when new versions ship. **Read at least three.** You'll never write a worse system prompt again.

### [`x1xhlol/system-prompts-and-models-of-ai-tools`](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
Same idea, different curator. Some overlap, some unique entries.

What you'll notice:
- They're long but every line earns its keep
- They use markdown headings and bullet structures relentlessly
- They tell the model what NOT to do as much as what to do
- They include examples — actual user/assistant exchanges

## Interactive tutorials

### [`anthropics/prompt-eng-interactive-tutorial`](https://github.com/anthropics/prompt-eng-interactive-tutorial)
Run as a Jupyter notebook. Nine chapters, takes ~3 hours, free. Goes deeper than most paid courses.

### [`anthropics/courses`](https://github.com/anthropics/courses)
Anthropic's broader course catalog — prompting, tool use, RAG, real-world workflows. All free.

## Frameworks worth knowing the names of

You'll see these techniques in the wild. Don't memorize them — recognize when they apply.

| Technique | When to use |
|-----------|-------------|
| **Chain-of-thought** | When the model needs to reason through steps. Just ask "think step by step" or "show your work." |
| **Few-shot** | Give 2–5 example input/output pairs in your prompt. Lifts performance more than longer instructions. |
| **ReAct** | Reason → Act (call tool) → Observe → Reason. The basic agent loop. |
| **Self-consistency** | Run the same prompt N times, take the majority answer. For when correctness matters. |
| **Plan-and-execute** | Force the model to plan all steps before executing any. Reduces wasted tool calls. |
| **Constitutional AI** | Have the model critique its own output against a rule set, then revise. |

## Eight named patterns worth knowing

These are the patterns you'll find yourself using in production prompts. Memorize the *names* so you can search for variations.

### 1. Read-before-write
```
Before suggesting changes, open and read the affected files. Cite the line
numbers of any code you reference. If you can't find what I'm referring to,
say so — don't guess.
```

### 2. Plan-then-act
```
Before making any code change, write a 2–3 sentence plan describing what
you'll change and why. Wait for me to confirm. Only then write code.
```

### 3. Propose-diff
```
Don't apply changes directly. Show me the diff you'd produce. I'll say
"go" before you write to disk.
```

### 4. Constrain-output
```
Reply ONLY with valid JSON matching this schema: {...}. No prose, no
markdown fences, no commentary.
```

### 5. One-shot example
```
Here's an example of a good response: <example>...</example>
Now do the same for the task below.
```

### 6. Explicit refusal grammar
```
If you cannot do the task safely, reply with REFUSED: <one-line reason>.
Do not attempt partial completion.
```

### 7. Self-critique
```
After producing your answer, critique it from the perspective of a senior
engineer reviewing a PR. List 3 things wrong with it. Then revise.
```

### 8. Scoped exploration
```
Look only in src/. Don't read tests/ or docs/. If the answer isn't in
src/, say "I'd need to look elsewhere" and stop.
```

These all show up — often combined — in the [leaked system prompts](https://github.com/asgeirtj/system_prompts_leaks) of real tools. The trick isn't inventing new patterns; it's recognizing which combination fits a given task.

## Patterns we use in `guarded_agent.py`

The system prompt in our agent uses three patterns from above:

1. **Role + scope declaration:** "You are a guarded coding agent. Your scope is {WORKSPACE}."
2. **Explicit capability and refusal grammar:** "Tools that return REFUSED:/NOT_FOUND: ... respect them."
3. **Negative constraints:** "You cannot run shell commands. You cannot access the network."

Pattern (3) is the trick. Telling the model what it *can't* do is often more important than telling it what it *can*. The list of things it can do is the `TOOLS` array — the model figures that out automatically. The list of things it can't do has to be stated.

## A short reading order for prompting fluency

If you're going to spend 5 hours getting better at this:

1. **Hour 1:** Read 3 leaked system prompts from the repos above
2. **Hour 2:** Anthropic prompt library — read the categories you care about
3. **Hour 3:** First two chapters of the Anthropic interactive tutorial
4. **Hour 4:** Read your own AI tool's docs on prompting (Cursor, Claude Code, whatever)
5. **Hour 5:** Build a small prompt library for your own work. Save every prompt that earned its keep.

## See also

- [`../starter/prompts/`](../starter/prompts/) — five reusable prompts to steal
- [`safeguards.md`](safeguards.md) — why "refusal grammar" matters when an agent can act
- [`tools.md`](tools.md) — the same patterns work across Cursor, Claude Code, Aider
