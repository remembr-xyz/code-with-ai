# Code With AI — SAIT Workshop

> **Build a guarded agent in 90 minutes.** Then take the workflow home.

Welcome. You're here because you came to the SAIT workshop on **May 27, 2026** — or because someone shared the link and you want the full kit. Either way, everything you need is in this repo.

This isn't "intro to ChatGPT." It's a hands-on workflow for shipping real code with AI tools, **with the guardrails on from day one**.

---

## What you'll leave with

- [x] Cursor installed and configured with a model you trust
- [x] **A guarded agent you built yourself** — scoped, tool-limited, audited
- [x] Your first `AGENTS.md` — the universal context file
- [x] A `.cursorrules` for your project
- [x] One MCP server installed and scoped properly
- [x] A mental model that scales to any AI coding tool
- [x] A bookmarks page worth ~6 months of self-study

---

## Tonight's structure

| Time | What | Where |
|------|------|-------|
| 6:00–6:25 | **Presentation** — How to code with AI | (auditorium) |
| 6:25–6:30 | Break + room setup | — |
| 6:30–6:40 | [Lab 0 — Setup](labs/00-setup.md) | — |
| 6:40–7:00 | [Lab 1 — `AGENTS.md` for your guarded agent](labs/01-agents-md.md) | — |
| 7:00–7:20 | [Lab 2 — MCP with scope limits](labs/02-mcp.md) | — |
| 7:20–7:40 | [Lab 3 — Build the guarded agent](labs/03-build-the-agent.md) | — |
| 7:40–7:55 | [Lab 4 — Red-team your guardrails](labs/04-red-team.md) | — |
| 7:55–8:00 | Show & tell + [Lab 5 (bonus) — Run it locally](labs/05-local-models.md) | — |

---

## Before you arrive

Five minutes of setup so we don't burn workshop time:

1. **Install [Cursor](https://cursor.sh)** — the AI-native editor. Free tier is fine.
2. **Sign up** — pick any model when prompted (we'll set up properly in Lab 0).
3. **Install Python 3.11+** — [python.org](https://www.python.org/downloads/) if you don't have it.
4. **Install Node.js 20+** — [nodejs.org](https://nodejs.org). Needed for some MCP servers.
5. **Bring a small project idea** — anything you've wanted to build. CLI tool. Scraper. Discord bot. Study helper. Doesn't matter. If you don't have one, we'll give you a menu.

That's it. Save the deeper installs (Ollama, etc.) for the bonus lab.

---

## What's a "guarded agent"?

An AI agent with **explicit, intentional guardrails**. Most beginner tutorials skip this and go straight to "give the AI all your files." Then your `~/Documents` gets nuked by a bad prompt.

A guarded agent has:

- **Scope** — it can only touch a specific folder
- **Tool allowlist** — it only uses tools you've explicitly enabled
- **Approval checkpoints** — destructive actions need your confirmation
- **Output filters** — no leaking secrets or PII
- **Cost limits** — won't run away with API calls
- **Audit trail** — every action logged

Real engineers don't ship unguarded agents to prod. Tonight, you learn to build with the rails on.

---

## Repo map

```
code-with-ai/
├── README.md                 ← you are here
├── starter/                  ← clone-or-copy starter for your project
│   ├── AGENTS.md             ← annotated template
│   ├── .cursorrules          ← annotated template
│   ├── .gitignore
│   ├── prompts/              ← example prompts that work
│   └── README.md
├── labs/                     ← do these in order
│   ├── 00-setup.md
│   ├── 01-agents-md.md
│   ├── 02-mcp.md
│   ├── 03-build-the-agent.md
│   ├── 04-red-team.md
│   └── 05-local-models.md    ← bonus
├── resources/                ← keep learning after tonight
│   ├── tools.md
│   ├── python-libs.md
│   ├── mcp-servers.md
│   ├── prompting.md
│   ├── safeguards.md
│   ├── local-models.md
│   └── further-reading.md
└── slides/                   ← the talk, exported
    └── workshop.pdf
```

---

## Already finished the workshop? Try this next

1. Run Lab 5 with a local model from [Ollama](https://ollama.com).
2. Pick three repos from [resources/further-reading.md](resources/further-reading.md) and skim them this week.
3. Take the `AGENTS.md` you wrote tonight and drop it into a real project at work or school. Watch your AI go from confused to surgical.
4. [Subscribe to Learn Agentic AI](https://learnagentic.substack.com) — I write daily about exactly this stuff.

---

## Who built this

Kanishk Patel — founder, [Founsi AI](https://founsi.ai) · writer, [Learn Agentic AI](https://learnagentic.substack.com) · find me on X [@above_almighty](https://x.com/above_almighty).

**Founsi AI** is the memory layer for your physical life. We catalog, track, and remember everything you own — so you don't have to. Currently raising pre-seed. If you're building with AI or you've ever lost something expensive, let's talk.

---

## License

MIT for everything in this repo. Use it, fork it, run your own workshop with it. Credit appreciated, not required.
