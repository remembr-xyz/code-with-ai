# MCP servers

> **TL;DR** Model Context Protocol servers — what to install, how to scope them, what to avoid. Start with `filesystem`. Read the [vetting checklist](#vetting-an-mcp-server-before-installing) before you `npm install` anything you didn't write.

For ready-to-paste configs, see [`../starter/examples/mcp/`](../starter/examples/mcp/).

## The official reference servers (verified 2026-05-26)

The [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) repo holds the **reference servers maintained by the MCP steering group**. Currently active:

| Server | What it does | Runtime | Scope flag |
|--------|--------------|---------|------------|
| [`filesystem`](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | Read/write files | Node (`npx`) | Root path as final arg |
| [`fetch`](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch) | Pull URLs into context | Python (`uvx`) | None — controls in code |
| [`git`](https://github.com/modelcontextprotocol/servers/tree/main/src/git) | Read branches, commits, diffs | Python (`uvx`) | Repo path as arg |
| [`sequentialthinking`](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | Structured scratchpad for hard problems | Node (`npx`) | None |
| [`memory`](https://github.com/modelcontextprotocol/servers/tree/main/src/memory) | Persistent key/value across sessions | Node (`npx`) | None — but see ASI06 |
| [`time`](https://github.com/modelcontextprotocol/servers/tree/main/src/time) | Timezone-aware time queries | Python (`uvx`) | None |
| [`everything`](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) | Demo server exposing all three primitives | Node (`npx`) | None |

> **Heads up:** the commonly cited `github` and `postgres` servers have been moved to [`servers-archived`](https://github.com/modelcontextprotocol/servers-archived) — they're no longer maintained by the steering group. Use community implementations from the official registry (below) instead.

### Start with these four

| Server | Why first |
|--------|-----------|
| `filesystem` | The wall. Scope-limited file access. Always your first MCP. |
| `fetch` | Lets the agent read external docs you point it at — without giving it a browser. |
| `git` | Read-only history is enough for most tasks. Don't add write to start. |
| `sequentialthinking` | Reasoning aid. Helps the model "think out loud" on hard problems. |

### Install pattern (Cursor)

In Cursor: Settings (⌘,) → MCP → edit `mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/abs/path/to/workspace"]
    }
  }
}
```

The path in `args` is the wall. **Absolute path only.** Restart Cursor after editing. Ready-to-paste configs for filesystem-scoped and the full starter kit live in [`../starter/examples/mcp/`](../starter/examples/mcp/).

## Where to find more

### Official discovery surface
- [`modelcontextprotocol/registry`](https://github.com/modelcontextprotocol/registry) — **the canonical "browse all servers" endpoint**. Start here.

### Third-party marketplaces
- [`smithery.ai`](https://smithery.ai) — popular marketplace with one-click install
- [`mcp.so`](https://mcp.so) — searchable directory

### Community-curated lists
- [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) — best-known
- [`appcypher/awesome-mcp-servers`](https://github.com/appcypher/awesome-mcp-servers) — second list, some unique entries

## Servers worth a look (community)

### Design
- **[Figma](../starter/examples/mcp/figma.md)** — first-party (Figma Desktop Dev Mode) or Framelink (community npm). Frames → React components.
- **[Stitch (Google)](https://smithery.ai/search?q=stitch)** — Google's design tool, similar pattern to Figma.

### Productivity
- **[Notion MCP](https://github.com/makenotion/notion-mcp-server)** — read/write Notion pages and DBs. Great for spec-driven coding from a Notion brief.
- **[Slack MCP](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack)** — archived but still works for read-only channel access.

### Data
- **Postgres / SQLite** — community implementations exist on the registry (the official ones are archived). **Always use a read-only DB user** for an MCP-connected DB.

### Code hosting
- **GitHub MCP** — community implementations exist on the registry. Scope your PAT to a single repo when possible.

## Servers to avoid installing on day one

These work, but they have sharp edges. Hold off until you've built your own agent end-to-end (Lab 3) and red-teamed it (Lab 4).

| Server | Why be careful |
|--------|----------------|
| `server-shell` (any variant) | Arbitrary shell. The unguarded-agent trap. |
| `server-git` *writes* (commit/push) | Easy to rewrite history. Restrict to read commands at first. |
| Anything with `--dangerously-skip-permissions` | Yes, this is a real flag in some servers. Don't. |

## Vetting an MCP server before installing

MCP servers run with your local privileges. A malicious one can read everything in scope. Before installing one you didn't write:

1. **Read the source.** Is it open? Published from a known organization?
2. **Check the npm/PyPI provenance.** Recent publish? Many downloads? Few maintainers?
3. **Pin the version.** Don't use floating tags like `@latest`.
4. **Scope tightly.** Filesystem MCP gets one path, never `/` or `~`.
5. **Read the tool list it exposes.** If it exposes 50 tools and you only need 2, prefer one that exposes 2.

This is OWASP ASI04 — Agentic Supply Chain Vulnerabilities. See [`safeguards.md`](safeguards.md) for the deeper story.

## Writing your own MCP server

Easier than it sounds. The spec is small.

- **Spec:** [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Python SDK:** [`github.com/modelcontextprotocol/python-sdk`](https://github.com/modelcontextprotocol/python-sdk)
- **TypeScript SDK:** [`github.com/modelcontextprotocol/typescript-sdk`](https://github.com/modelcontextprotocol/typescript-sdk)

Minimal Python server (20 lines):

```python
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("my-server")

@app.list_tools()
async def list_tools():
    return [{"name": "hello", "description": "say hi", "inputSchema": {...}}]

@app.call_tool()
async def call_tool(name, args):
    if name == "hello":
        return [{"type": "text", "text": f"hello, {args.get('who', 'world')}"}]

async def main():
    async with stdio_server() as (r, w):
        await app.run(r, w, app.create_initialization_options())
```

Drop that in `mcp.json` with `"command": "python", "args": ["my_server.py"]` and Cursor picks it up.

## Scope discipline checklist

When you install any new MCP server, ask:

- [ ] What's the **smallest scope** that lets it do the job?
- [ ] Does it need **write** access or only **read**?
- [ ] What **secrets** does it have access to?
- [ ] Is there a **dry-run / read-only** mode I can use first?
- [ ] If it goes haywire, what's the **blast radius**?

## See also

- [`../labs/02-mcp.md`](../labs/02-mcp.md) — Lab 2 walks you through installing your first MCP
- [`../starter/examples/mcp/`](../starter/examples/mcp/) — working configs
- [`safeguards.md`](safeguards.md) — OWASP ASI04, vetting at depth
