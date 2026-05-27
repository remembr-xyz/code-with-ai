# MCP — Model Context Protocol

> **TL;DR** [MCP](https://modelcontextprotocol.io/) is Anthropic's open standard for plugging external capabilities into AI clients. Cursor, Claude Code, Codex, Continue — they all speak it. This folder has working configs for the four servers every beginner should install first.

## What an MCP server can expose (from slide 19)

| Primitive | What it is | Example |
|---|---|---|
| **Tools** | Functions the model can call | `read_file`, `run_query`, `send_message` |
| **Resources** | Read-only data the model can fetch | A config file, a record set, a Notion doc |
| **Prompts** | Templated workflows the user can trigger | `/summarize_pr`, `/file_bug` |

Sequential-thinking is a *Prompt* (a reasoning aid), not a *Tool*. Filesystem is a classic Tool server. Most servers expose Tools.

## The official starters (verified 2026-05-26)

The [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers/tree/main/src) repo holds only **reference servers maintained by the MCP steering group**:

| Server | Purpose | Runtime |
|---|---|---|
| [`filesystem`](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Read/write files, scoped to one folder. **Start here.** | Node (`npx`) |
| [`fetch`](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Pull URLs into context | Python (`uvx`) |
| [`git`](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Read branches, commits, diffs | Python (`uvx`) |
| [`sequentialthinking`](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | Structured scratchpad for hard problems | Node (`npx`) |
| [`memory`](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | Persistent key/value memory across sessions | Node (`npx`) |
| [`time`](https://github.com/modelcontextprotocol/servers/tree/main/src/time) | Timezone-aware time queries | Python (`uvx`) |
| [`everything`](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) | Demo server exposing all three primitives | Node (`npx`) |

> **Heads up:** `github` and `postgres` are commonly cited but have been moved to [`servers-archived`](https://github.com/modelcontextprotocol/servers-archived) — they're no longer maintained by the steering group. For those, use community implementations from the registry.

## Where to find more

| Catalog | What it is |
|---|---|
| [`modelcontextprotocol/registry`](https://github.com/modelcontextprotocol/registry) | **The official discovery surface.** Start here if you want "browse all servers." |
| [`smithery.ai`](https://smithery.ai) | Popular third-party marketplace with one-click install |
| [`mcp.so`](https://mcp.so) | Third-party searchable directory |
| [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) | Community-curated list |

The slide deck (page 21) lists smithery.ai, mcp.so, the official MCP repo, and awesome-mcp-servers as the four marketplaces.

## Working configs in this folder

| File | What it does |
|---|---|
| [`filesystem-scoped.json`](filesystem-scoped.json) | The exact example from slide 22 — filesystem MCP rooted to one folder |
| [`full-starter-kit.json`](full-starter-kit.json) | All four "must-have" starters in one config (filesystem, fetch, git, sequential-thinking) |
| [`figma.md`](figma.md) | Figma MCP setup — both first-party (Figma Desktop Dev Mode) and Framelink (community npm) |

To use any of these in Cursor:

1. Cursor → Settings (⌘,) → search "MCP" → click "MCP Servers"
2. Cursor opens `mcp.json`. Paste in the contents from one of these files
3. Adjust the path (e.g. `/Users/you/sait-workshop` → your actual path)
4. Save. Look for the green dot in the MCP list (= server is running)
5. Open a new chat. The server's tools are now available

If a server fails to start: most failures are missing `npx`/`uvx` or a wrong path.

## How to vet an MCP server before installing

MCP servers run with your local privileges. A malicious one can read everything in scope. Before installing one you didn't write:

1. **Read the source.** Is it open? Is it published from a known organization?
2. **Check the npm/PyPI provenance.** Recent publish? Many downloads? Few maintainers?
3. **Pin the version.** Don't use floating tags like `@latest`.
4. **Scope tightly.** Filesystem MCP gets one path, never `/` or `~`.
5. **Read the tool list it exposes.** If it exposes 50 tools and you only need 2, prefer one that exposes 2.

This is OWASP ASI04 — Agentic Supply Chain Compromise. See [`../../../resources/safeguards.md`](../../../resources/safeguards.md) for the deeper story.

## See also

- [Slide 22](../../../slides/workshop.pdf) — the exact filesystem-scoped example
- [`../../../labs/02-mcp.md`](../../../labs/02-mcp.md) — Lab 2 walks you through installing one
- [`../../../resources/mcp-servers.md`](../../../resources/mcp-servers.md) — broader survey of useful MCPs
