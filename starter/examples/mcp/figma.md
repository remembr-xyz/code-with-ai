# Figma MCP — two ways to set it up

> **TL;DR** Two distinct options. Don't mix them up. Pick one.

| Option | What it is | When to use |
|---|---|---|
| **Figma Desktop's Dev Mode MCP** | First-party server, built into Figma | You have Figma Desktop installed and a Dev Mode seat |
| **Framelink** (`figma-developer-mcp`) | Third-party community npm package | You don't have Dev Mode, or want lighter-weight setup |

---

## Option 1 — Figma's first-party Dev Mode MCP

Canonical docs: [developers.figma.com/docs/figma-mcp-server/local-server-installation](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)

**Setup (~2 minutes):**

1. Open **Figma Desktop** → Preferences → enable **Dev Mode MCP Server**
2. Note the local URL Figma reports (typically `http://127.0.0.1:3845/mcp`)
3. In Cursor → Settings → MCP, add:

```json
{
  "mcpServers": {
    "figma": {
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

4. Restart Cursor. Open a Figma frame in Figma Desktop.
5. In Cursor, ask: *"Using Figma, fetch the currently selected frame and write a React component matching the layout."*

**Requires:** Figma Desktop app + an active Dev Mode seat on the Figma account.

---

## Option 2 — Framelink (community npm package)

Package: [`figma-developer-mcp` on npm](https://www.npmjs.com/package/figma-developer-mcp) · Repo: [`GLips/Figma-Context-MCP`](https://github.com/GLips/Figma-Context-MCP)

**Setup (~3 minutes):**

1. Get a Figma Personal Access Token: Figma → Settings → Account → Personal access tokens → **Generate**. Scope: at minimum **File content (read)**.
2. Add to your `mcp.json`:

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp", "--stdio"],
      "env": {
        "FIGMA_API_KEY": "figd_..."
      }
    }
  }
}
```

3. Restart Cursor. Ask: *"Using Figma, fetch frame [Figma URL] and write a React component matching the layout."*

**Works with:** Figma browser version. No Dev Mode seat needed.

---

## Things to know

- Both servers expose frames as **Resources** the model can fetch, plus a handful of Tools (`get_file`, `get_node`)
- The model still has to write the React/Vue/Svelte. The MCP just gives it the raw layer tree, styles, and tokens — it doesn't auto-generate components
- For pure design-to-code with a tighter feedback loop, see [`../../../resources/figma-experiments.md`](../../../resources/figma-experiments.md)
- The slide deck reference: appendix A7 ([slide 39](../../../slides/workshop.pdf))

## Security note

Your Figma PAT is an API key. Treat it like one:
- Never commit `mcp.json` with a real token in it
- Scope it to **read** only (don't grant write)
- Rotate it if it leaks
