# `/starter` — Your project's starting point

Copy this whole folder into your own project. The files here are **annotated templates** — they have heavy comments explaining each section so you know what to customize and what to leave alone.

## What's in here

| File | What it does | When to edit |
|------|--------------|--------------|
| `AGENTS.md` | The universal context file. Cursor, Claude Code, and Codex all read it. | Edit it for your project before your first prompt. |
| `.cursorrules` | Cursor-specific operating rules. Run-on-every-prompt instructions. | Edit when you've found a pattern that should always apply. |
| `.gitignore` | Standard ignores + workshop-specific entries. | Add to it as needed. |
| `prompts/` | Example prompts that work well. Steal them. | Add your own as you discover good ones. |

## Quick start (during the workshop)

```bash
# From the repo root:
cp -r starter ~/my-workshop-project
cd ~/my-workshop-project
git init
cursor .
```

Then go to [Lab 1](../labs/01-agents-md.md) and customize the `AGENTS.md`.
