# `/starter` — Your project's starting point

Copy this whole folder into your own project. The files here are **annotated templates** — they have heavy comments explaining each section so you know what to customize and what to leave alone.

## What's in here

| File | What it does | When to edit |
|------|--------------|--------------|
| [`AGENTS.md`](AGENTS.md) | The universal context file. Cursor, Claude Code, and Codex all read it. | Edit it for your project before your first prompt. |
| [`.cursorrules`](.cursorrules) | Cursor-specific operating rules. Run-on-every-prompt instructions. | Edit when you've found a pattern that should always apply. |
| `.gitignore` | Standard ignores + workshop-specific entries. | Add to it as needed. |
| [`prompts/`](prompts/) | Example prompts that work well. Steal them. | Add your own as you discover good ones. |
| [`examples/`](examples/) | **Inspiration gallery** — real `AGENTS.md` / `.cursorrules` / `mcp.json` / `CLAUDE.md` from production repos, annotated. | Read, don't edit. |
| [`guarded_agent.py`](guarded_agent.py) | Reference Python implementation of a guarded agent — read the source to see how the loop works. | Read; modify in Lab 3 if you want. |

## Quick start (during the workshop)

```bash
# From the repo root:
cp -r starter ~/my-workshop-project
cd ~/my-workshop-project
git init
cursor .
```

Then go to [Lab 1](../labs/01-agents-md.md) and customize the `AGENTS.md`. If you want inspiration before writing your own, the [`examples/`](examples/) folder has seven real `AGENTS.md` files from production repos — pick the smallest (`sst/opencode`, ~4 KB) and read it end-to-end.
