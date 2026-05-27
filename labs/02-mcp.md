# Lab 2 — MCP, scoped

> **TL;DR** Install the filesystem MCP server scoped to your workshop folder. Confirm the wall holds: in-scope reads work, out-of-scope reads get refused. Optionally add a second server. Ready-to-paste configs in [`../starter/examples/mcp/`](../starter/examples/mcp/).

**Time:** 20 minutes (7:00–7:20)
**Goal:** Install the filesystem MCP server, configure it to *only* see your project folder, and confirm the scope holds. By the end you'll have an agent that can read and write files — but only the ones you said it could.

> Lab 1 was about telling the AI what it *should* do. Lab 2 is about making sure it *can't* do anything else.

---

## What MCP actually is

MCP — Model Context Protocol — is a small standard, shipped by Anthropic in late 2024, for how AI clients talk to external tools. Think USB for agents. Cursor, Claude Code, Codex, Cline, every serious tool now speaks it.

An MCP server is a tiny program that exposes a set of capabilities (`list_files`, `read_file`, `fetch_url`, `query_database`). Your AI client picks them up automatically and the model can call them like functions.

The killer feature for our purposes: every MCP server **takes its scope as a config argument**. The filesystem server, for example, takes a root path. Pass it `~/sait-workshop` and it physically cannot touch `~/Documents`. That's the safeguard. It's not a polite request — it's a wall.

---

## Step 1 — Install Node.js if you haven't (1 min)

Most MCP servers run on Node. Check:

```bash
node --version
```

If you see `v20.x` or higher, you're set. If not, install from [nodejs.org](https://nodejs.org). LTS is fine.

---

## Step 2 — Configure the filesystem MCP server (5 min)

In Cursor, open Settings (`Cmd/Ctrl + ,`) → search for **MCP** → click **MCP Servers**. You'll see an `mcp.json` file (or a "Add new MCP server" button that creates one).

Paste this, replacing the path with your actual workshop folder:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/sait-workshop"
      ]
    }
  }
}
```

**Critical:** that last path is the scope boundary. The server will refuse to read or write anything outside it. Use the *full absolute path* — no `~`, no relatives.

Save the file. Cursor will start the server in the background; you'll see "filesystem" appear in the MCP servers list with a green dot once it's running.

---

## Step 3 — Confirm the scope is real (5 min)

This is the most important step of the night. We're going to verify the wall actually holds.

Open a Cursor chat (`Cmd/Ctrl + L`) and run these prompts, one at a time:

### Prompt 1 — inside the scope (should succeed)

```
Using the filesystem tool, list every file in my workshop folder
and tell me how many there are.
```

You should see the agent call the filesystem tool, get a list back, and answer. Good.

### Prompt 2 — outside the scope (should fail)

```
Using the filesystem tool, read /Users/YOUR_USERNAME/Documents/passwords.txt
(or any file you know exists in your home directory but outside the
workshop folder). What does it contain?
```

You should see the agent attempt the read and the MCP server refuse — usually with an error like "path is outside allowed directories." If the agent shrugs and tries to summarize from memory, ask it explicitly: *"What error did you actually receive from the tool?"*

**If the read succeeds, the scope is broken.** Go back to Step 2 and verify:
1. The path in `mcp.json` is your workshop folder, not `/` or `~`
2. The path is absolute (no `~`)
3. You restarted Cursor after saving the config

---

## Step 4 — Add a second MCP server (5 min, optional)

If the filesystem server works, add one more so the agent can fetch URLs. This is genuinely useful for "summarize this article" tasks and it's a one-liner.

The fetch server is a Python package (run via `uvx`) — different from filesystem's `npx`. If you don't have `uvx`, install it: `curl -LsSf https://astral.sh/uv/install.sh | sh`.

Update `mcp.json` to:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/sait-workshop"
      ]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

For the full 4-server starter kit (filesystem + fetch + git + sequential-thinking), see [`../starter/examples/mcp/full-starter-kit.json`](../starter/examples/mcp/full-starter-kit.json).

Then test:

```
Using the fetch tool, get https://agents.md and tell me in three
sentences what AGENTS.md is supposed to contain.
```

You should see the page fetched, summarized, three sentences delivered. Welcome to a model that can read the live web.

---

## Step 5 — Update your AGENTS.md to reflect the new capability (2 min)

Open the `AGENTS.md` you wrote in Lab 1 and update Section 7 (Scope):

```markdown
## 7. Scope boundary (for this agent)

- Working directory: /Users/YOUR_USERNAME/sait-workshop/
- Filesystem MCP: rooted at the working directory (enforced)
- Fetch MCP: can pull URLs (model decides which)
- Tools NOT installed: git, shell-execute, GitHub MCP, anything else.
  If you need a capability not in this list, ask me to add it.
```

That last line is the move. The AI now has explicit instructions about what it *doesn't* have. No more silent "I'll just try this shell command" surprises.

---

## Two MCP servers worth knowing about, but NOT installing yet

You'll see these in tutorials and want to install them. Don't. They have sharp edges that bite beginners. We'll cover them properly in Lab 4.

- **`mcp-server-git` (write mode)** — gives the agent commit/push/branch access. Power tool. Wrong setup and the agent rewrites your history. Read-only mode is in the [full-starter-kit.json](../starter/examples/mcp/full-starter-kit.json) — that's fine.
- **`server-shell` (any variant)** — runs arbitrary shell commands. This is the unguarded-agent trap.

If you want them later, install them with explicit scope limits and a strict allow-list in your AGENTS.md. For now, filesystem + fetch is plenty.

---

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| "filesystem" doesn't show in Cursor's MCP list | Restart Cursor. The config is read on startup. |
| Red dot / "failed to start" | Run `npx -y @modelcontextprotocol/server-filesystem /your/path` in a terminal and read the actual error |
| Out-of-scope read succeeds | Path in config is wrong — check it's absolute and the right folder |
| Agent says "I don't have access to MCP tools" | Try `@filesystem` to invoke the server explicitly, or check Cursor's MCP toggle in chat |
| `npx` not found | Install Node.js from [nodejs.org](https://nodejs.org) |

---

## When you're done

You should have:

- An `mcp.json` with filesystem (and optionally fetch) configured
- A demonstrated scope: in-scope reads work, out-of-scope reads get refused
- An updated `AGENTS.md` Section 7 that explicitly lists what the agent has

Next: [Lab 3 — Build the guarded agent](03-build-the-agent.md). We're going to write the actual Python script that ties it all together — and now you've got the tool layer to plug it into.

## Going deeper

- [`../starter/examples/mcp/`](../starter/examples/mcp/) — ready-to-paste configs (filesystem-scoped, full starter kit, Figma)
- [`../resources/mcp-servers.md`](../resources/mcp-servers.md) — the broader survey of useful MCPs + vetting checklist
- [`../starter/examples/mcp/figma.md`](../starter/examples/mcp/figma.md) — Figma MCP setup (both first-party and community npm)
- [modelcontextprotocol.io](https://modelcontextprotocol.io) — the spec itself, ~30-min read
