# `starter/examples/` — the inspiration gallery

> **TL;DR** Curated, real-world examples of the four files you'll write tonight. Every link points to an actual file in an actual public repo — nothing fictional. Read three of them end-to-end and you'll learn more than from any tutorial.

The deck (slide 33) tells you to read three real `AGENTS.md` files end-to-end — this folder is where you find them, with annotations explaining what's worth noticing in each.

## What's in here

| Folder | What it covers |
|---|---|
| [`agents-md/`](agents-md/) | Real `AGENTS.md` from production repos — **7 cross-stack picks** (openai/codex, sst/opencode, vercel/ai, apache/airflow, etc.) **plus a "by language" section** with verified examples for Python, React Native, Kotlin, Swift, Go, Rust |
| [`cursor-rules/`](cursor-rules/) | Cursor rules — legacy `.cursorrules` **and** modern `.cursor/rules/*.mdc`, **plus deep links by language** into `awesome-cursorrules` (Python, React Native, Kotlin, Swift, Go, Rust) |
| [`mcp/`](mcp/) | Ready-to-paste `mcp.json` configs (filesystem-scoped, full starter kit, Figma) + the verified list of MCP starters as of May 2026 |
| [`claude-md/`](claude-md/) | How `CLAUDE.md` relates to `AGENTS.md` — short answer: `@AGENTS.md` import |

## How to use this folder

**If you're a beginner:** start with [`agents-md/`](agents-md/). Pick the smallest real example ([`sst/opencode`](https://github.com/sst/opencode/blob/dev/AGENTS.md), ~4 KB). Read it top-to-bottom. Then read your [`starter/AGENTS.md`](../AGENTS.md) template. The shape will click.

**If you've used Cursor before:** jump to [`cursor-rules/`](cursor-rules/) for the `.mdc` directory pattern that big projects have moved to.

**If you're here for the MCP servers:** [`mcp/`](mcp/) has working configs. Copy, paste, adjust the path.

**If you use Claude Code:** read [`claude-md/`](claude-md/) — the recommended pattern is one line in CLAUDE.md that imports your AGENTS.md.

## Ground rule

Nothing in this gallery is invented. Every example links to a real file in a public repo, verified on the date in the file. If an upstream repo changes substantially, the annotations may go stale — file an issue and we'll refresh.
