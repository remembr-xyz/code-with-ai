# Labs

Six labs, in order. Each runs 10–20 minutes. Together they take you from "Cursor installed" to "guarded agent shipped, red-teamed, and optionally running offline."

| # | Lab | Time | What you walk away with |
|---|-----|------|-------------------------|
| 00 | [Setup](00-setup.md) | 10 min | Cursor open, model picked, project folder ready |
| 01 | [`AGENTS.md`](01-agents-md.md) | 20 min | A real context file, customized for your project |
| 02 | [MCP, scoped](02-mcp.md) | 20 min | One MCP server installed and locked to your project root |
| 03 | [Build the agent](03-build-the-agent.md) | 20 min | Cursor running as your guarded agent + tightened `.cursorrules` based on observation |
| 04 | [Red team](04-red-team.md) | 15 min | You break your own guardrails, then patch them |
| 05 | [Local models](05-local-models.md) *(bonus)* | 5–15 min | The same agent, running offline via Ollama |

## How to use these

- **Live at the workshop:** follow along during the 6:30–8 PM block. Each lab opens at the time on the table.
- **Reading later:** the labs are standalone. Lab 0 will catch you up regardless of when you find this.
- **Stuck on one:** skip to the next. Each lab tells you what you should have at the end, so you can resume from a clean state.

## Common questions

**Do I need to finish all of them?**
No. Labs 0–3 are the spine. Lab 4 is the most important if you ever plan to deploy an agent. Lab 5 is genuinely bonus.

**Can I do these without paying for an API?**
Yes. The entire core path (Labs 0–4) runs on Cursor's bundled inference — no API keys, no payment. Lab 5 is free after the model download. If you want to *also* run the Python reference agent in Lab 3, [Groq's free tier](https://console.groq.com/) handles it without a credit card.

**What if I'm faster than the timing?**
Each lab has a "stretch goal" or "Option B" path. Use it. Or jump to a resource page from [`resources/`](../resources/).

**What if I'm slower?**
Lab 0 has a troubleshooting table. After that, ask your neighbor or the facilitator. The labs don't penalize you for stopping mid-way — pick up where you left off.
