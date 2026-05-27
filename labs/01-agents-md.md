# Lab 1 — `AGENTS.md` for your guarded agent

> **TL;DR** Fill in the 9-section template for your project, with explicit guardrails (especially Section 6). 20 minutes. Skim 1–2 real `AGENTS.md` from [`../starter/examples/agents-md/`](../starter/examples/agents-md/) first if you want inspiration.

**Time:** 20 minutes (6:40–7:00)
**Goal:** Customize the starter `AGENTS.md` for *your* project, with explicit guardrails. By the end, Cursor should reference your file when answering questions about your project.

> This is the single most valuable file you'll write tonight. If you only finish one lab, finish this one.

If you want inspiration before writing yours, the [`../starter/examples/agents-md/`](../starter/examples/agents-md/) folder has 7 real `AGENTS.md` files from production repos (openai/codex, sst/opencode, vercel/ai, apache/airflow, etc.) annotated with what's worth noticing in each. Read the shortest one ([`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md), ~4 KB) before you start.

---

## What you're building

A working `AGENTS.md` for the project idea you picked in Lab 0, framed as **a guarded agent**: scoped, tool-limited, with explicit do/don'ts.

The starter template has 9 sections with placeholders and comments. We'll customize each one.

---

## Step 1 — Open the starter

```bash
cd ~/sait-workshop
cursor AGENTS.md
```

You'll see the template with `[SQUARE BRACKET PLACEHOLDERS]` and `<!-- HTML COMMENTS -->`. The HTML comments are notes from us — the AI ignores them. You can keep them or delete them.

---

## Step 2 — Sections 1–5: the basics (10 min)

Work through these in order. **Don't aim for perfect — aim for real.** You'll refine later.

### Section 1: What this project is

One paragraph, plain English.

**Bad:**
> A scalable, AI-powered platform for next-generation knowledge management.

**Good:**
> A CLI that summarizes PDFs in a folder. Built for me, to clear my Downloads. Pre-MVP, just running locally.

### Section 2: Tech stack

The 3–5 libraries that matter. Skip the obvious ones.

If you haven't installed anything yet, list what you *plan* to use. You can update it later.

### Section 3: How to run/test/build

The exact commands. Even if your project is empty right now, fill this in with what you *expect* the commands to be:

```bash
pip install -r requirements.txt
python -m myapp
pytest
```

Future-you will thank you. So will the AI.

### Section 4: File map

If your project is empty, write the structure you *plan* to have. Sketch it now:

```
myapp/
├── src/main.py
├── tests/
└── data/
```

This becomes the AI's mental map of your code. When it doesn't know where something should go, it'll look here.

### Section 5: Conventions

5–10 bullets max. Things that aren't obvious from the code.

If you're not sure, copy the defaults from the template and pick three to actually enforce.

---

## Step 3 — Section 6: Guardrails (5 min) — the most important section

This is where the **guarded agent** comes alive. You're going to write the rules that make the AI safe to let loose on your code.

### Your DO list

Write 3 explicit DO rules. Examples worth stealing:

- **Explain before editing.** Plan first, write code second.
- **Run tests after every change to `src/`.**
- **Read before guessing.** When unsure how something works, open the file.
- **Keep diffs small.** One change per turn.
- **Log shell commands** before running them.

### Your DON'T list

This is where you protect yourself. Write at least 3 explicit DON'Ts.

**Always include these three** (they save you from real disasters):

- **Never run `rm -rf`, `git push --force`, `git reset --hard`, or anything destructive without asking.**
- **Never modify `.env`, `secrets/`, or anything in `.gitignore`.**
- **Never invent libraries.** If importing, confirm it's installed.

Then add 2–3 project-specific ones. Examples:

- "Never run database migrations without showing me the SQL first."
- "Never modify the auth module — that's a closed area for now."
- "Don't reformat existing files. Touch only what I asked you to change."

---

## Step 4 — Section 7: Scope (2 min) — the most underrated section

Define WHERE the agent can operate. Fill in the actual paths:

```
- Working directory: /Users/yourname/sait-workshop/
- Read access: everything in the working dir EXCEPT .env, secrets/, .gitignore matches
- Write access: same
- Network access: only api.anthropic.com (or whichever provider)
- Shell commands: pip, npm, pytest only — destructive commands need confirmation
```

This is the **scope boundary**. In Lab 2 we'll make the AI actually respect this with MCP. For now, just declaring it is half the battle — Cursor will keep itself inside this box if you say so.

---

## Step 5 — Test it (3 min)

Save the file. Then open a new Cursor chat (Cmd/Ctrl + L) and ask:

> "Without making changes, summarize what this project is and what I should NOT do as an AI working on it."

**What you want to see:** the AI cites your AGENTS.md. It mentions your guardrails. It correctly states the scope.

**If it doesn't:**
- Check that AGENTS.md is in the project root (not a subfolder)
- Restart Cursor (closes and reopens the context)
- Make sure the file is saved (Cmd/Ctrl + S)

---

## Stretch goal (if you finish early)

Add a **Section 8 — Known gotchas** entry. Make one up if you don't have a real incident yet:

> "Don't use `eval()` on user input — this got us once and we banned it."

Then ask the AI to write a function that takes user input. Watch it avoid `eval()` automatically. That's institutional memory in action.

---

## Common pitfalls

| Problem | Fix |
|---------|-----|
| AI ignores AGENTS.md | File must be in project root. Restart Cursor. |
| AI follows it but you disagree with its interpretation | Make the rule sharper. Vague rules get vague obedience. |
| File is getting too long (>200 lines) | Cut it. Less is more. Move details into README. |
| Same rule needs to apply across ALL your projects | Move it to Cursor's global rules (Settings → Rules) |

---

## When you're done

You should be staring at:
- A customized `AGENTS.md` saved in your project root
- A Cursor chat where the AI just demonstrated it's reading your file
- A clearer sense of what "guarded" actually means

**Tap your neighbor. Quick swap — show each other your DON'T lists. You'll learn from theirs.** Next: [Lab 2 — MCP with scope limits](02-mcp.md).

## Going deeper

- [`../starter/examples/agents-md/`](../starter/examples/agents-md/) — 7 real `AGENTS.md` files, annotated. Read three end-to-end.
- [`../starter/examples/claude-md/`](../starter/examples/claude-md/) — how Claude Code's `CLAUDE.md` relates (one-line `@AGENTS.md` import)
- [agents.md](https://agents.md/) — the cross-tool spec itself
