# MCP servers

Model Context Protocol servers — what to install, how to scope them, what to avoid.

## The official reference servers

[`github.com/modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) — Anthropic's reference implementations, all `@modelcontextprotocol/server-*`.

### Start with these four

| Server | What it does | Scope flag |
|--------|--------------|------------|
| `server-filesystem` | Read/write files | Takes a root path as final arg |
| `server-fetch` | Pull URLs into context | None — controls in code |
| `server-git` | Branch/commit/diff (read-only operations safer than writes) | Repo path as arg |
| `server-sequential-thinking` | Adds a scratchpad for hard reasoning | No scope needed |

### Install pattern (Cursor)

In Cursor: Settings → MCP Servers → edit `mcp.json`:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/abs/path/to/workspace"]
    },
    "fetch": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-fetch"]
    }
  }
}
```

The path in `args` is the wall. Absolute path only. Restart Cursor after editing.

## Servers worth a look (community)

### Productivity
- **[`mcp-server-github`](https://github.com/modelcontextprotocol/servers/tree/main/src/github)** — issue/PR access. Token-scoped.
- **[`mcp-server-slack`](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)** — channel reads/writes. Token-scoped.
- **[`mcp-notion`](https://github.com/makenotion/notion-mcp-server)** — Notion read/write. Workspace-scoped.

### Data
- **[`mcp-server-postgres`](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres)** — read-only SQL. **Always use a read-only DB user.**
- **[`mcp-server-sqlite`](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)** — local SQLite.

### Search / web
- **[`mcp-server-brave-search`](https://github.com/modelcontextprotocol/servers/tree/main/src/brave-search)** — web search via Brave's API.
- **[`mcp-server-puppeteer`](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer)** — headless browser. Powerful, careful.

### Community directories
- **[`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers)** — curated big list
- **[`appcypher/awesome-mcp-servers`](https://github.com/appcypher/awesome-mcp-servers)** — second curated list
- **[`mcp.so`](https://mcp.so)** — searchable directory

## Servers to avoid installing on day one

These work but they have sharp edges. Hold off until you've built your own agent end-to-end (Lab 3) and red-teamed it (Lab 4).

| Server | Why be careful |
|--------|----------------|
| `server-shell` (any variant) | Arbitrary shell. This is the unguarded-agent trap. |
| `server-git` *writes* (commit/push) | Easy to rewrite history. Restrict to read commands at first. |
| Anything with `--dangerously-skip-permissions` | Yes, this is a real flag in some servers. Don't. |

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
