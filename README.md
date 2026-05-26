# code-with-ai

> Build a guarded agent in 90 minutes. Workshop materials from the SAIT session, May 27, 2026.

A guarded agent is an AI agent with rails on. Scoped to a folder. Locked to an allow-list of tools. Forced to ask before it does anything destructive. Logs every action.

Most coding-with-AI tutorials teach you to type a prompt and let the model rip. Then someone follows that advice, points an agent at their home directory, and watches `.zshrc` get rewritten in real time. This repo is the antidote.

You'll build a guarded agent from scratch tonight — in Python or whatever you brought. You'll write the `AGENTS.md` that makes it trustworthy. You'll install one MCP server and scope it correctly. You'll try to break your own guardrails. And if there's time, you'll swap the brain for a model running entirely on your laptop.

## A taste of what you'll write

Every section of your `AGENTS.md` matters, but Section 6 is the one most beginner tutorials skip. Yours will look something like this:

```markdown
## 6. Guardrails

### Don'ts (non-negotiable)
- Never run `rm`, `git push --force`, or `git reset --hard` without asking
- Never modify `.env`, `secrets/`, or anything in `.gitignore`
- Never invent libraries — grep `requirements.txt` first
- Never refactor "while you're at it" — fix what I asked, nothing more

### Dos
- Explain the plan in 2–3 sentences before non-trivial edits
- Run `pytest` after every change to `src/` and show me the output
- Read before guessing — open the file if you're unsure
- Keep diffs small; one concern per turn
```

That's the spirit of the night. Constraints first. Capability second.

## Quick start

```bash
git clone https://github.com/remembr-xyz/code-with-ai.git
cd code-with-ai
cp -r starter ~/my-workshop-project
cd ~/my-workshop-project
cursor .   # open in Cursor, then go to labs/00-setup.md
```

## Tonight's run-of-show

Talk runs 6:00–6:25 in the auditorium. Doors open at 5:45. Labs start at 6:30 sharp.

| # | When | Lab | What you walk away with |
|---|------|-----|-------------------------|
| 00 | 6:30–6:40 | [Setup](labs/00-setup.md) | Cursor open, model picked, project folder ready |
| 01 | 6:40–7:00 | [`AGENTS.md`](labs/01-agents-md.md) | A real context file, customized for your project |
| 02 | 7:00–7:20 | [MCP, scoped](labs/02-mcp.md) | One MCP server installed and locked to your project root |
| 03 | 7:20–7:40 | [Build the agent](labs/03-build-the-agent.md) | Cursor running as your guarded agent — observed, rules tightened |
| 04 | 7:40–7:55 | [Red team](labs/04-red-team.md) | You break your own guardrails, then patch them |
| 05 | 7:55–8:00 | [Local models](labs/05-local-models.md) *(bonus)* | The same agent, running offline via Ollama |

If you finish early or you're reading from home, the labs work standalone. Each one takes 15–20 minutes.

## What's in this repo

```
README.md               You are here.
starter/                Copy this folder into your own project.
  AGENTS.md             Annotated 9-section template. Customize in Lab 1.
  .cursorrules          Short focused operating rules.
  .gitignore            Secrets discipline.
  prompts/              5 reusable prompts. Steal them.
labs/                   Six labs in order. Don't skip 00.
resources/              Curated reading. No filler.
  tools.md              Cursor, Claude Code, Aider, Continue, opencode
  python-libs.md        anthropic, openai, pydantic-ai, instructor
  mcp-servers.md        The four every beginner needs + how to scope them
  prompting.md          Anthropic prompt library, leaked system prompts, more
  safeguards.md         The deeper checklist from Lab 4
  local-models.md       Ollama, LM Studio, llamafile + recommended models
  further-reading.md    Newsletters, people to follow, papers worth your time
slides/                 The presentation, exported.
```

The most important file in the repo is `starter/AGENTS.md`. Read it before the workshop if you want a head start.

## Before Wednesday — 5 minutes of prep

1. Install [Cursor](https://cursor.sh). **Free tier is enough — no API keys needed.**
2. Install [Node.js 20+](https://nodejs.org). The MCP servers we use are Node-based.
3. Bring a project idea. Anything. CLI tool, scraper, Discord bot, study helper. If you don't have one, Lab 0 hands you a menu.

That's it for the core path. The whole workshop runs on Cursor's bundled inference; you do not need an Anthropic or OpenAI key.

Python 3.11+ is only needed if you want to read and modify the reference agent code in Lab 3 (which you can do with Cursor's help — you don't need to run it). Ollama and LM Studio are bonus-lab-only.

## After the workshop, do these three things this week

1. Take the `AGENTS.md` you wrote tonight and drop it into a real project at school or work. Watch the AI go from confused to surgical.
2. Pick three repos from [`resources/further-reading.md`](resources/further-reading.md) and skim them. Skimming is fine — none of these are textbooks.
3. Subscribe to [Learn Agentic AI](https://learnagentic.substack.com). I write daily about exactly this stuff and the workshop barely scratches the surface.

## Who built this

Kanishk Patel — founder of [Founsi AI](https://founsi.ai), writer of [Learn Agentic AI](https://learnagentic.substack.com), arguing about prompts on X as [@above_almighty](https://x.com/above_almighty).

**Founsi AI** is the memory layer for your physical life. We catalog, track, and remember everything you own — so you don't have to. Currently raising pre-seed. If you build with AI or you've ever lost something expensive, find me after the workshop.

## License

MIT. Fork it, run your own workshop with it, change anything you want. Credit appreciated, not required.
