# Tools

> **TL;DR** Cursor is the workshop default. Claude Code if you prefer terminal. Aider if you want maximum control. Continue if you want local-first. Everything else is a variation on those four. Comparison table at the bottom.

The shortlist of AI coding tools worth your time, with honest notes on when to use which.

## The big four

### [Cursor](https://cursor.sh)
The default for this workshop. VS Code fork, AI-native. Best balance of agent capabilities, codebase-aware chat, and polish. Free tier covers most students; Pro is $20/mo if you outgrow it. **Pick this first.**

### [Claude Code](https://docs.claude.com/en/docs/claude-code)
Anthropic's terminal-native coding agent. Lives in your shell, no editor lock-in, scriptable. Best when you want AI in your loop without changing your editor (Neovim users, this is you). Free with Pro/Max Claude subscription.

### [Codex](https://platform.openai.com/docs/codex)
OpenAI's coding agent. Strong with GPT-5, browser/sandbox tooling, decent multi-file work. Best if your team is already deep on OpenAI APIs.

### [Aider](https://aider.chat)
Pure terminal, git-aware, model-agnostic. Auto-commits every change with descriptive messages. Best when you want maximum control and audit trail.

## Open-source alternatives

### [Cline](https://github.com/cline/cline)
VS Code extension. Open-source. Bring your own API key (Anthropic, OpenAI, Ollama, etc.). Less polish than Cursor, more transparency.

### [Roo Code](https://github.com/RooVetGit/Roo-Cline)
Cline fork with extra modes, MCP-friendly. Active development. Worth a look if you want more than Cline ships with.

### [opencode](https://github.com/sst/opencode)
From the SST team. Self-hosted, terminal + web UI, multi-model. Newer, very promising. Try when you want to own the whole stack.

### [Continue.dev](https://continue.dev)
VS Code + JetBrains extension. Open-source. Strongest local-model story (native Ollama support). Use when you don't want a fork — Continue plugs into the editor you already have.

## Other tools you'll hear about

| Tool | When to consider |
|------|------------------|
| **GitHub Copilot** | Pure autocomplete in your existing editor. Stops short of agentic. |
| **Cody (Sourcegraph)** | Strong at large codebase search. Enterprise leaning. |
| **JetBrains AI** | If you live in IntelliJ/PyCharm and don't want to leave. |
| **Windsurf (Codeium)** | Editor like Cursor. Currently behind on agentic features. |
| **Zed AI** | Lightweight editor with built-in AI. Worth watching. |

## Configs and templates to steal

You'll write better `AGENTS.md` and `.cursorrules` files faster by reading other people's.

- **[`PatrickJS/awesome-cursorrules`](https://github.com/PatrickJS/awesome-cursorrules)** — the canonical community library of `.cursorrules` files, searchable by stack. Bookmark this.
- **[`cursor.directory`](https://cursor.directory)** — searchable directory of `.cursorrules`, MCP setups, and full project templates. Better UX than the awesome list.
- **[`anthropics/skills`](https://github.com/anthropics/skills)** — Anthropic's official "Skills" repo: examples of how to teach Claude specific procedures with markdown + scripts. Worth studying even if you don't use Skills directly.
- **[`anthropics/anthropic-cookbook`](https://github.com/anthropics/anthropic-cookbook)** — recipes for common patterns: tool use, structured outputs, RAG, classification. Skim chapter by chapter.

## Official docs worth reading once

- **[docs.cursor.com](https://docs.cursor.com)** — Cursor's docs. The "Agent" and "Rules" pages are mandatory.
- **[Cursor forum](https://forum.cursor.com)** — bug reports, tips, real-world usage. Search before posting.
- **[docs.claude.com/claude-code](https://docs.claude.com/en/docs/claude-code)** — Claude Code's docs. The "hooks", "slash commands", and "MCP servers" pages are the deepest.
- **[`anthropics/claude-code`](https://github.com/anthropics/claude-code)** — the Claude Code repo. Read the SDK docs if you want to build your own coding agent on top of it.
- **[modelcontextprotocol.io](https://modelcontextprotocol.io)** — the MCP spec. 30-minute read, demystifies the whole protocol.

## How to actually pick

Three questions:

1. **Do you live in a terminal or an editor?** Terminal → Claude Code / Aider. Editor → Cursor / Cline / Continue.
2. **Do you want maximum agency or maximum control?** Agency (let it rip, fix later) → Cursor. Control (every change reviewed) → Aider / Claude Code.
3. **Are you running cloud or local?** Cloud → any of these. Local-first → Continue + Ollama, or Aider with `ollama/llama3.1`.

There's no wrong answer at the workshop level. Tonight we used Cursor because it's the friendliest entry point.

## Comparison at a glance

| Tool | Pricing | Best feature | MCP support | Local models | Best for |
|---|---|---|---|---|---|
| [Cursor](https://cursor.sh) | Free / $20 mo | Inline edits + chat in one editor | ✅ | ⚠️ (custom URL) | Workshop default, day-to-day work |
| [Claude Code](https://code.claude.com) | Free with Claude Pro/Max | Terminal-native, hooks, skills | ✅ | ❌ | Terminal lovers, scriptable workflows |
| [Codex](https://platform.openai.com/docs/codex) | Pay-per-use | Strong with GPT-5 | ⚠️ partial | ❌ | OpenAI-deep teams |
| [Aider](https://aider.chat) | Free + API costs | Auto-commits, git-native, model-agnostic | ⚠️ partial | ✅ | Max control + audit trail |
| [Cline](https://github.com/cline/cline) | Free + API costs | Open-source, transparent | ✅ | ✅ | Inspectable agent loop |
| [Continue](https://continue.dev) | Free + API costs | Best local-model story | ✅ | ✅ | VS Code + Ollama |
| [opencode](https://github.com/sst/opencode) | Free + API costs | Self-hosted, web UI option | ✅ | ✅ | Own-the-stack folks |

## See also

- [`../starter/examples/cursor-rules/`](../starter/examples/cursor-rules/) — `.cursor/rules/*.mdc` patterns from real production repos
- [`prompting.md`](prompting.md) — same prompt patterns work across tools
- [`safeguards.md`](safeguards.md) — tool-agnostic guardrails
