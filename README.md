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

## How to use this repo

Three audiences. Pick the path that fits:

### You're attending the workshop tonight

Just follow [`labs/00-setup.md`](labs/00-setup.md). Everything is timed to the run-of-show below. Skip the rest until after.

### You're reading from home

Start with [`labs/`](labs/) — the labs are standalone and total ~90 minutes. After (or instead): the [`resources/`](resources/) folder has the curated reading list with a 30-day plan.

### You just want the templates

Go straight to [`starter/examples/`](starter/examples/). It's the inspiration gallery — real `AGENTS.md`, `.cursorrules`, `mcp.json`, and `CLAUDE.md` files from production repos (openai/codex, sst/opencode, vercel/ai, apache/airflow, supabase, shadcn-ui, and others), each annotated with what's worth noticing.

### You want examples for *your* language

Both the [AGENTS.md gallery](starter/examples/agents-md/README.md#by-language) and the [cursor-rules gallery](starter/examples/cursor-rules/README.md#by-language--deep-links-into-awesome-cursorrules) have **"by language" sections** covering:

- **Python** — pydantic-ai, ruff, uv, airflow, langchain (+ 13 awesome-cursorrules entries)
- **React Native** — gesture-handler, react-native-firebase, repack (+ Expo/Expo-Router rules)
- **Kotlin** — IntelliJ Community, Ktor, Now in Android (+ Ktor, Spring Boot, Jetpack Compose rules)
- **Swift / iOS** — Vapor, stripe-ios (+ SwiftUI and UIKit rules) ⚠️ ecosystem adoption is thin
- **Go** — Kubernetes, Grafana, Prometheus (+ generic + REST + Temporal rules)
- **Rust** — uv (Rust internals), Deno (CLAUDE.md), Rerun (+ 2 generic rule files)
- **TypeScript / Node** — sst/opencode, vercel/ai, openai/codex, browser-use

All entries verified to exist with byte sizes on 2026-05-27.

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
README.md                       You are here.
starter/                        Copy this folder into your own project.
  AGENTS.md                     Annotated 9-section template. Customize in Lab 1.
  .cursorrules                  Short focused operating rules.
  .gitignore                    Secrets discipline.
  guarded_agent.py              ~200-line reference Python agent. Read it.
  prompts/                      5 reusable prompts. Steal them.
  examples/                     ★ Inspiration gallery (curated real examples)
    agents-md/                  7 real AGENTS.md from production repos, annotated
    cursor-rules/               .cursorrules + .cursor/rules/ patterns in the wild
    mcp/                        Ready-to-paste MCP configs (filesystem, full kit, Figma)
    claude-md/                  CLAUDE.md vs AGENTS.md, the @AGENTS.md import pattern
labs/                           Six labs in order. Don't skip 00.
resources/                      Curated reading. No filler.
  README.md                     Index with 4 reading-order paths
  tools.md                      Cursor, Claude Code, Aider, Continue, opencode, Cline
  python-libs.md                anthropic, openai, pydantic-ai, litellm, evals, observability
  mcp-servers.md                The 4 starter MCPs + registry + vetting checklist
  prompting.md                  Anthropic prompt library, 8 named patterns, leaked prompts
  safeguards.md                 ★ Lethal Trifecta + 5 real incidents + OWASP ASI Top 10
  local-models.md               Ollama, LM Studio + recommended models by RAM tier
  repos-to-study.md             Reference agents worth cloning
  further-reading.md            Newsletters, people, papers, books, 30-day plan
  figma-experiments.md          Full-app Figma → code experiments
  glossary.md                   ★ Every term in the workshop, defined
slides/                         The presentation, exported.
CONTRIBUTING.md                 How to suggest improvements
```

★ = added or substantially expanded since the original scaffold. The most important file in the repo is `starter/AGENTS.md`; the second-most is `resources/safeguards.md`.

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

## Skill ladder — where to go from here

| You are… | Read in this order |
|---|---|
| **A beginner just out of the workshop** | 1. [`resources/glossary.md`](resources/glossary.md) (5 min). 2. [`resources/safeguards.md`](resources/safeguards.md) → Lethal Trifecta + Five Guards sections. 3. Drop your AGENTS.md into a real project this week. |
| **An intermediate dev who wants depth** | 1. Read 3 real AGENTS.md from [`starter/examples/agents-md/`](starter/examples/agents-md/). 2. [`resources/prompting.md`](resources/prompting.md) → 8 named patterns. 3. [`resources/repos-to-study.md`](resources/repos-to-study.md) → pick 2 reference agents. |
| **Building your own agent** | 1. [`starter/guarded_agent.py`](starter/guarded_agent.py) → read end-to-end. 2. [`resources/python-libs.md`](resources/python-libs.md). 3. [`resources/safeguards.md`](resources/safeguards.md) → OWASP ASI Top 10. 4. Build it. |
| **Privacy-first / offline** | 1. [`labs/05-local-models.md`](labs/05-local-models.md). 2. [`resources/local-models.md`](resources/local-models.md). 3. [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) for ongoing updates. |
| **Going to ship to production** | All of [`resources/safeguards.md`](resources/safeguards.md). [Anthropic Claude Code best practices](https://code.claude.com/docs/en/best-practices). [12-Factor App](https://12factor.net/). |

## Who built this

Kanishk Patel — founder of [Founsi AI](https://founsi.ai), writer of [Learn Agentic AI](https://learnagentic.substack.com), arguing about prompts on X as [@above_almighty](https://x.com/above_almighty).

**Founsi AI** is the memory layer for your physical life. We catalog, track, and remember everything you own — so you don't have to. Currently raising pre-seed. If you build with AI or you've ever lost something expensive, find me after the workshop.

## License

MIT. Fork it, run your own workshop with it, change anything you want. Credit appreciated, not required.
