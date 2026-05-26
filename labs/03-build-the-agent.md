# Lab 3 — Make Cursor your guarded agent

**Time:** 20 minutes (7:20–7:40)
**Goal:** Stop thinking of "the agent" as a thing you'll build someday. **Cursor + your AGENTS.md + your scoped MCP server *is* the guarded agent.** This lab is where you make that real and prove it to yourself.

> Up to here you've configured pieces. This lab is where you watch them work together — and where you understand what an agent actually is at the code level if you want to look under the hood later.

---

## The reframe

You came in expecting we'd "build an AI agent in Python." We're going to do that *as optional reading material* at the end. But the more useful truth is this:

> **An AI agent is a loop: LLM → tool call → result → LLM → repeat.** Cursor is already that loop. Your `AGENTS.md` is the briefing. Your `.cursorrules` are the operating rules. Your scoped filesystem MCP is the tool layer. You've already built a guarded agent. It's running right now.

This lab makes the agent prove it.

---

## Step 1 — Give Cursor a real job (5 min)

Pick a small, real task for your guarded agent — Cursor. The point is to watch it use *only* the tools you allowed, *only* in the scope you set, and to ask before doing anything destructive.

Some options (steal one or invent your own):

| Task | Why it's a good test |
|------|----------------------|
| "Read every file in my project and write a one-paragraph summary to `OVERVIEW.md`" | Exercises read + write + scope |
| "Find every TODO comment in the codebase and put them in a `TODO.md` checklist" | Reads broadly, writes one new file |
| "Create a `prompts/` folder with three example prompts I could reuse" | Pure write, tests creation flow |
| "Refactor `AGENTS.md` so the Don'ts list is tighter — but show me a diff first" | Tests the 'plan before edit' rule from your `.cursorrules` |

Open Cursor's Agent panel (the right sidebar, click "Agent" mode), paste your task, hit send. **Don't approve auto-run yet — watch each step.**

---

## Step 2 — Watch the loop (5 min)

You should see something like this:

```
1. Agent reads AGENTS.md (your briefing)
2. Agent reads .cursorrules (your operating rules)
3. Agent uses the filesystem MCP to list files
4. Agent reads specific files
5. Agent proposes a plan (because your .cursorrules said "explain before non-trivial edits")
6. Agent waits for your approval
7. Agent writes the new file
8. Agent confirms what it did
```

That's the agent loop you've heard about. There's no magic — your `AGENTS.md` told it the rules, your scoped MCP gave it tools, Cursor wired them together.

**Notice the guards firing:**

- The plan-before-edit rule from your `.cursorrules` → the agent explained instead of just writing
- The scope from your MCP config → the agent could only see your workshop folder
- The Don'ts in `AGENTS.md` → the agent didn't `rm` anything, didn't touch `.env`, didn't push to git

This is the workshop's whole point. Working guardrails, observable behavior, no surprises.

---

## Step 3 — Tighten one rule based on what you saw (5 min)

Watching Cursor work usually reveals something it did that you didn't like. Maybe it was too eager, or it skipped the plan, or it summarized a file you wanted left alone.

Open `.cursorrules` and add **one** new rule based on what you observed. Examples:

- "When creating new files, ask which folder they should go in first"
- "When summarizing, never overwrite an existing file — append with a separator"
- "When you see a `.env.example`, use it as a template; never read a real `.env`"
- "If a task affects more than 5 files, propose a split before starting"

Save, then re-run a similar task. Confirm the new rule fires.

This is how good `.cursorrules` files grow — one rule per observed pain. Don't try to anticipate everything upfront.

---

## Step 4 (optional, 5 min) — Look under the hood

If you want to see what an agent looks like at the code level, open [`starter/guarded_agent.py`](../starter/guarded_agent.py) in Cursor. It's a ~200-line Python implementation of exactly the loop you just watched Cursor run.

Have Cursor walk you through it:

```
Open guarded_agent.py and explain each section in three sentences.
What are the six guardrails this code implements?
```

You'll get a tour of `in_scope`, `is_secret`, `approve`, `audit`, `TOOLS`, and the main loop. **That's the code that's running, conceptually, inside Cursor every time you chat with it.**

### Want to actually run the Python agent?

The script auto-detects which provider you have set up and uses it. Pick the lowest-friction path:

**Path A — Just simulate it in Cursor (zero install).**
Ask Cursor: *"Walk through what would happen if I ran `guarded_agent.py` with the prompt 'summarize AGENTS.md.' Simulate each tool call and show me the resulting trace."* Cursor will hand-simulate the agent loop. Same understanding, no setup.

**Path B — Groq, free, no credit card (~3 min).**
Best path if you want to actually see your agent execute.

1. Get a key at [console.groq.com/keys](https://console.groq.com/keys) (no card required)
2. `pip install openai`
3. `export GROQ_API_KEY=gsk_...`
4. `python guarded_agent.py "summarize the AGENTS.md in this folder"`

The script detects `GROQ_API_KEY` and uses Llama 3.1 8B on Groq. Fast (~500 tokens/sec) and free.

**Path C — Ollama, local, fully offline (~5 min).**
If you already have Ollama (or did Lab 5 first):

```bash
ollama pull qwen2.5-coder:7b
pip install openai
python guarded_agent.py "your prompt"
```

The script falls back to Ollama at `localhost:11434` when no other key is set.

**Path D — OpenAI or Anthropic key.**
If you have credit on either: just `export OPENAI_API_KEY=...` (auto-detected) or follow the Anthropic swap instructions in the comment block at the bottom of `guarded_agent.py`.

None of these are required for the workshop. They're for after, if you want to extend the agent.

---

## What you should have at the end

- A Cursor session where you gave the agent a real task and watched it use only the tools and scope you allowed
- A `.cursorrules` with at least one new rule you added based on observation
- A clearer mental model of the agent loop (LLM ↔ tool ↔ result)
- Optionally: a working Python agent if you went down the Groq/Anthropic/OpenAI path

You've built a guarded agent. It's running. Lab 4 is where you try to break it.

Next: [Lab 4 — Red team your guardrails](04-red-team.md).
