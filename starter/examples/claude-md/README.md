# `CLAUDE.md` vs `AGENTS.md`

> **TL;DR** `CLAUDE.md` is Claude Code's project-memory file. `AGENTS.md` is the cross-tool community standard. Claude Code reads `CLAUDE.md` natively. The recommended pattern is a one-line `CLAUDE.md` that imports your `AGENTS.md` — that way every tool sees the same briefing and you keep one source of truth.

Canonical Claude Code docs: [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)

## The recommended pattern

If you already have an `AGENTS.md`, your `CLAUDE.md` can be a one-liner:

```markdown
# Project memory for Claude Code

@AGENTS.md

## Claude-specific additions

- Use the `verify` skill before claiming a PR is ready
- Default to Opus for refactors >50 lines, Sonnet for everything else
- Prefer Plan mode (Shift+Tab) for any task spanning >3 files
```

The `@AGENTS.md` import inlines the AGENTS.md content. One source of truth, two file extensions.

## Memory hierarchy (Claude Code reads, in priority order)

| Scope | Path | What goes in |
|---|---|---|
| **Managed** | Provided by IDE/enterprise | Locked rules — your org sets these |
| **User** | `~/.claude/CLAUDE.md` | *Your* preferences across all projects |
| **Project** | `<repo>/CLAUDE.md` | This project's briefing |
| **Local** | `<repo>/CLAUDE.local.md` (gitignored) | Personal notes not for the team |

Plus path-scoped rules in `<repo>/.claude/rules/*.md` with frontmatter (similar to `.cursor/rules/*.mdc`).

## A real example you can read

[`vercel/ai/CLAUDE.md`](https://github.com/vercel/ai/blob/main/CLAUDE.md) — identical content to their [AGENTS.md](https://github.com/vercel/ai/blob/main/AGENTS.md). They keep them in sync (likely via symlink or copy in CI). A pragmatic way to support both audiences with one source of truth.

## What Anthropic does *not* publish

There is no official "flagship CLAUDE.md to copy from" in any Anthropic repo. The [`anthropics/claude-code`](https://github.com/anthropics/claude-code) repo has a `.claude/` directory for plugin scaffolding but no public `CLAUDE.md` at root.

The canonical reference is the [memory docs page](https://code.claude.com/docs/en/memory) itself, which includes:
- Recommended sections
- The ~200-line size target (anything longer gets ignored over time)
- `@path` import syntax
- AGENTS.md interop guidance

## Bottom line for the workshop

**Write an `AGENTS.md`.** That covers every tool — Cursor, Codex, Claude Code, others.

If you use Claude Code and want Claude-specific extras (a different style of feedback, skill preferences, etc.), add a small `CLAUDE.md` that:
1. Imports `@AGENTS.md` on its first line
2. Adds the Claude-only bits below

That's it. Two files, one source of truth, every tool happy.

## See also

- [`../agents-md/`](../agents-md/) — the AGENTS.md gallery
- [code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory) — canonical CLAUDE.md docs
- [agents.md](https://agents.md/) — the cross-tool standard
